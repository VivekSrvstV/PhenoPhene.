import zipfile

import pandas as pd
import os
import pathlib
import subprocess

import psycopg2
from flask import render_template


class dbcon:

    connection = psycopg2.connect(database="phenophene",
                            host="localhost",
                            user="postgres",
                            password="vivek2022",
                            port=5432)
    def create(request):
        if request.method == 'POST':
            cursor = dbcon.connection.cursor()
            # Get data from POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            # Insert data into database
            cursor.execute("INSERT INTO your_table_name (name, email) VALUES (%s, %s)", [name, email])
            #return redirect('list')
        return render_template('create.html')

    def read(request):
        cursor = dbcon.connection.cursor()
        try:
            cursor.execute("SELECT * FROM plant_details")
            rows = cursor.fetchall()
            return rows
            # Process the results or do other operations
        except Exception as e:
            print(f"Error: {e}")
            # If needed, roll back the transaction
            cursor.execute("ROLLBACK;")


    def getTableData(request, table_name):
        cursor = dbcon.connection.cursor()
        # Check if the table exists
        #exists = cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        #cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
        #exists = cursor.fetchone()[0]
        exists = f"SELECT EXISTS(SELECT 1 FROM {table_name})"
        cursor.execute(exists)
        print(exists)
        exists_result = cursor.fetchone()[0]
        # If the table exists, perform the query
        if exists_result:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            # Process the fetched rows here
            print(f"The table '{table_name}'  exist.")

            columns = [col[0] for col in cursor.description]
            print(columns)

            return columns, rows
        else:
            print(f"The table '{table_name}' does not exist.")
            rows = 0
            columns = 0
            return rows,columns


    def getSearchQuery(request, search_val):
        dbcon.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
        cursor = dbcon.connection.cursor()
        try:
            cursor.execute("SELECT table_name, qtl_table, snp_table FROM plant_details")

        except Exception as e:
            dbcon.connection.rollback()  # Rollback the transaction on error
            print(f"Error: {e}")



        #cursor.execute("SELECT table_name,qtl_table, snp_table FROM plant_details")
        result = cursor.fetchall()
        phenotype_data = []
        qtl_data = []
        snp_data = []

        for item in result:
            phenotype_data.append(item[0])
            if item[1]:
                qtl_data.append(item[1])
            if item[2]:
                snp_data.append(item[2])

        #print("Phenotype Data:", phenotype_data)
        #print("QTL Data:", qtl_data)
        #print("SNP Data:", snp_data)


        combined_list = []
        combined_list.extend(phenotype_data)
        combined_list.extend(qtl_data)
        combined_list.extend(snp_data)

        print("Combined List:", combined_list)
        results = []
        columns = ""
        # Execute a query to get a list of tables in the database
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        tables = cursor.fetchall()

        combined_list_lower = [value.lower() for value in combined_list]
        table_names_lower = [table[0].lower() for table in tables]

        filtered_values = [value for value in combined_list_lower if value in table_names_lower]
        print('filetered tables : -----',filtered_values)
        search_results = []

        for table in filtered_values:
            try:
                print('tables ----',table)
                cursor.execute(f"SELECT * FROM {table}")
                columns = [col[0] for col in cursor.description]
                where_clause = ' OR '.join([f'"{col}" LIKE %s' for col in columns])

                query = f"SELECT * FROM {table} WHERE {where_clause}"
                search_vals = ["'%" + search_val + "%'" for i in range(len(columns))]
                query_with_params = query % tuple(search_vals)
                print(query_with_params)
                cursor.execute(query_with_params)
                filtered_rows = cursor.fetchall()
                search_results.append({"tablename": table,
                                "cols": columns,
                                "rows": filtered_rows})
                print(filtered_rows)
            except psycopg2.Error as e:
                #search_results[table] = f"Error: {e}"
                print(e)
        print('--------------------------------------------',filtered_rows)
        '''try:
            for tablename in filtered_values:
                print(tablename)
                cursor.execute(f"SELECT * FROM {tablename}")

                columns = [col[0] for col in cursor.description]
                where_clause = ' OR '.join([f'"{col}" LIKE %s' for col in columns])

                query = f"SELECT * FROM {tablename} WHERE {where_clause}"
                search_vals = ["'%"+search_val+"%'" for i in range(len(columns))]
                query_with_params = query % tuple(search_vals)
                print(query_with_params)
                cursor.execute(query_with_params)
                filtered_rows = cursor.fetchall()
                results.append({"tablename": tablename,
                                "cols": columns,
                                "rows": filtered_rows})
            return results
        except psycopg2.Error as e:
                print(f"An error occurred: {e}")
                #dbcon.connection.rollback()

        print('==================RESULT===========================',results)'''
        return search_results

    def download_selected_tables(request,tn):
        # Customize the following command based on your MySQL setup
        cmd = f"mysqldump -u <root> -p <phenophene> {tn}"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if error:
            # If there was an error in the command execution, handle it accordingly
            # For example, you can raise an exception or return an error response
            return HttpResponse("Error occurred while exporting the table.", status=500)

        response = HttpResponse(output, content_type='application/sql')
        response['Content-Disposition'] = f'attachment; filename="{tn}.sql"'
        print("code is completed here")
        return response
    def download_selected_table(request,tn):

        cursor = dbcon.connection.cursor()
        cursor.execute(f"SELECT p.table_name,p.qtl_table,p.snp_table FROM plant_details p where p.table_name='{tn}'")
        rows = cursor.fetchall()
        phenotype = rows[0][0]
        qtl = rows[0][1]
        snp = rows[0][2]
        phenotype_data = []
        qtl_data = []
        snp_data = []
        if(phenotype):
            cursor.execute(f"SELECT * FROM {phenotype}")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            phenotype_data = pd.DataFrame(rows, columns=columns)
            phenotype_data.to_excel(f"downloads/{phenotype}.xlsx", index=False)
        if (qtl):
            cursor.execute(f"SELECT * FROM {qtl}")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            qtl_data.append({"cols": columns, "rows": rows})
        if (snp):
            cursor.execute(f"SELECT * FROM {snp}")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            snp_data.append({"cols": columns, "rows": rows})
        response = download_file_code(tn,phenotype,qtl,snp)
        return response
    def download_file_code(tn, p, q, s):
        # Build the file's absolute path
        filename = "Phenotype_Maize_Pace.xlsx"
        file_path = os.path.abspath("downloads/"+filename)
        # Check if the file exists
        if os.path.exists(file_path):

            # Open the file for reading
            with open(file_path, 'rb') as f:
                # Build the response object
                response = HttpResponse(f.read())
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
                return response
        # If the file doesn't exist, return a 404 error
        else:
            raise Http404
        #return response

    def update(request, id):
        cursor = dbcon.connection.cursor()
        if request.method == 'POST':
            # Get data from POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            # Update data in database
            cursor.execute("UPDATE your_table_name SET name=%s, email=%s WHERE id=%s", [name, email, id])
            return redirect('list')
        cursor.execute("SELECT * FROM your_table_name WHERE id=%s", [id])
        row = cursor.fetchone()
        return render(request, 'update.html', {'data': row})

    def delete(request, id):
        cursor = dbcon.connection.cursor()
        cursor.execute("DELETE FROM your_table_name WHERE id=%s", [id])
        return redirect('list')
    def test(request):
        folder_name = "downloads"
        files_to_download = ["{}.xlsx".format(tn), "{}.xlsx".format(q), "{}.xlsx".format(s)]

        # specify the directory containing the files
        directory = os.path.abspath(folder_name)
        if not os.path.isdir(directory):
            return HttpResponse("Error: {} is not a valid directory".format(directory))

        # create a zip archive and add only specific files in the directory
        archive_name = "{}.zip".format(folder_name)
        archive = zipfile.ZipFile(archive_name, "w")
        for filename in files_to_download:
            file_path = os.path.join(directory, filename)
            if os.path.exists(file_path):
                archive.write(file_path, filename)
            else:
                print("File {} not found in directory {}".format(filename, directory))
        archive.close()
        download_dir = str(pathlib.Path.home() / "Downloads")
        # create response object and set the content type
        response = HttpResponse(File(open(archive_name, 'rb')), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.join(download_dir, "{}.zip".format(folder_name)))
