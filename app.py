#!/usr/bin/env python
from flask import Flask
from flask import Flask, render_template, request, redirect, send_file, send_from_directory, session
import subprocess
from dbcon import dbcon
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import os
from dash import Dash, dcc, html, Input, Output
import dash_bio as dashbio
import dash
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import mplcursors
import io
import base64
import matplotlib
matplotlib.use('agg')

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Change this to a secure random key

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TEMPLATES'] = 'templates'

from flask_wtf import FlaskForm
from wtforms import StringField

class SearchForm(FlaskForm):
    search_input = StringField('Search a Phenotype')


@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/analyse')
def analyse():
    return render_template('analyse.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/browse')
def browse():
    rows = dbcon.read(request)

    return render_template('browse.html', data=rows)

@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/correlation')
def correlation():
    return render_template('correlation.html')

@app.route('/correlation_detail')
def correlation_detail():
    # Your view logic here
    return render_template('correlation_detail.html')


@app.route('/transformation_details')
def transformation_details():
    # Your view logic here
    return render_template('transformation_details.html')

@app.route('/correlation_results', methods=['POST'])
def correlation_results():
    input_search = request.form.get('inputsearch')
    # Add logic to process the form submission and display results
    return render_template('correlation_results.html', input_search=input_search)


@app.route('/snp_viewer')
def snp_viewer():
    return render_template('snp_viewer.html')

@app.route('/qtl_viewer')
def qtl_viewer():
    return render_template('qtl_viewer.html')




@app.route('/downloadXlsx/<filename>')
def download_file(filename):
    # Assuming the 'downloads' folder is in the same directory as your Flask app
    file_path = f"downloads/{filename}"
    return send_file(file_path, as_attachment=True)
@app.route('/download')
def download():
    rows = dbcon.read(request)
    print(rows)
    return render_template('download.html', data=rows)
'''
   <!-- <td style="font-size: x-large; color: #0b5ed7;">{{ row.name }} <em>({{ row.file }})</em></td>
                    <td><a href="{{ url_for('static', filename='downloads/' + row.file) }}" download><img src="{{ url_for('static', filename='images/download_link.png') }}" style="width: 50px; height: 50px;"/> </a></td>
               -->
'''
@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_input = request.form['search_input']
        print(search_input)
        results  = dbcon.getSearchQuery(request, search_input)
        print('???????????????????????????????result???????????????????????????????',results)
        return render_template("search_result.html",  res=results)

    else:
        return render_template("search.html")



@app.route('/search_details')
def search_details():
    # Sample data, replace this with your actual data
    result_data = [
        {
            'tablename': 'Table1',
            'cols': ['Column1', 'Column2', 'Column3'],
            'rows': [
                ['Value11', 'Value12', 'Value13'],
                ['Value21', 'Value22', 'Value23'],
            ]
        },
        {
            'tablename': 'Table2',
            'cols': ['ColumnA', 'ColumnB', 'ColumnC'],
            'rows': [
                ['ValueA1', 'ValueB1', 'ValueC1'],
                ['ValueA2', 'ValueB2', 'ValueC2'],
            ]
        },
        # Add more tables as needed
    ]

    return render_template('search_details.html', res=result_data)

@app.route('/browser')
def browser():
    return render_template('index.html')


@app.route('/visualise')
def visualize():
    return render_template('visualise.html')



@app.route('/plant_details/<table_name>')
def plant_details(table_name):
    print("table names", table_name)
    if table_name != "None":
        columns, rows = dbcon.getTableData(request, table_name)
        print("columns", columns)
        print("rows", rows)
        return render_template("plant_details.html", columns=columns, rows=rows)
    else:
        print(table_name)
        print("No table found")
        message = "Data not found !!! "
        print('im into else')
        rows = dbcon.read(request)
        return render_template('browse.html', data=rows, message=message)



@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        # Get data from POST request
        name = request.form['name']
        email = request.form['email']
        # Insert data into database (replace 'your_table_name' with your actual table name)
        cursor.execute("INSERT INTO your_table_name (name, email) VALUES (%s, %s)", [name, email])
        return redirect('list')
    return render_template('create.html')

@app.route('/read')
def read():
    # Select all data from 'plant_details' table
    cursor.execute("SELECT * FROM plant_details")
    rows = cursor.fetchall()
    return rows

@app.route('/getTableData/<table_name>')
def get_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return render_template('table_data.html', columns=columns, rows=rows)

@app.route('/getSearchQuery/<search_val>')
def get_search_query(search_val):
    # Your existing search logic here...
    return results

@app.route('/downloadSelectedTable/<tn>')
def download_selected_table(tn):
    # Your existing download logic here...
    return send_from_directory('downloads', f'{tn}.xlsx', as_attachment=True)

@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    cursor.execute("SELECT * FROM your_table_name WHERE id=%s", [id])
    row = cursor.fetchone()
    if request.method == 'POST':
        # Get data from POST request
        name = request.form['name']
        email = request.form['email']
        # Update data in database
        cursor.execute("UPDATE your_table_name SET name=%s, email=%s WHERE id=%s", [name, email, id])
        return redirect('list')
    return render_template('update.html', data=row)

@app.route('/delete/<id>')
def delete(id):
    cursor.execute("DELETE FROM your_table_name WHERE id=%s", [id])
    return redirect('list')

@app.route('/test')
def test():
    # Your existing test logic here...
    return send_file('downloads/{}.zip'.format(folder_name), as_attachment=True)





UPLOAD_FOLDER = '/var/www/html/PhenoPhene/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return render_template('visualise.html', message='No file selected')

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        session['file_path'] = file_path

        df = pd.read_csv(file_path)
        columns = df.columns.tolist()

        return render_template('visualise.html', message='File uploaded successfully', file_path=file_path, columns=columns)

    return render_template('visualise.html', message='Upload failed')


@app.route('/plot', methods=['POST'])
def plot():
    uploaded_file = session.get('file_path')
    if uploaded_file is None or not os.path.exists(uploaded_file):
        return render_template('visualise.html', message='No file uploaded yet')

    df = pd.read_csv(uploaded_file)

    columns = df.columns.tolist()
    df.columns = df.columns.str.lower()

    x_axis = request.form.get('x_axis').lower()
    y_axis = request.form.get('y_axis').lower()

    if not x_axis or not y_axis:
        return render_template('visualise.html', message='Please select both X-axis and Y-axis', columns=columns)

    if 'plot_button' in request.form:
        fig = go.Figure(data=[go.Bar(x=df[x_axis], y=df[y_axis])])
        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'histogram_button' in request.form:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df[x_axis], name=x_axis))
        fig.add_trace(go.Histogram(x=df[y_axis], name=y_axis))

        fig.update_layout(
            title_text='Histogram',
            xaxis_title_text=x_axis,
            yaxis_title_text='Frequency'
        )

        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'boxplot_button' in request.form:
        # Assuming 'df' is your DataFrame loaded from the CSV file
        fig = go.Figure()
        fig.add_trace(go.Box(y=df[y_axis], name=y_axis))

        fig.update_layout(
            xaxis=dict(title=x_axis),
            yaxis=dict(title=y_axis),
            title=f'Box Plot of {y_axis} vs {x_axis}',
            showlegend=True
        )

        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'scatter_plot_button' in request.form:
        color_column = request.form.get('color_column', None)
        size_column = request.form.get('size_column', None)
        hover_data = request.form.getlist('hover_data')

        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_column, size=size_column, hover_data=hover_data)
        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'violin_plot_button' in request.form:
        color_column = request.form.get('color_column', None)

        fig = px.violin(df, y=y_axis, color=color_column, box=True, points='all', hover_data=df.columns)
        fig.update_traces(width=10)
        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'line_chart_button' in request.form:
        x_axis = request.form.get('x_axis').lower()
        y_axis = request.form.get('y_axis').lower()

        if not x_axis or not y_axis:
            return render_template('visualise.html', message='Please select both X-axis and Y-axis', columns=columns)

        x_values = np.array(df[x_axis])
        y_values = np.array(df[y_axis])

        fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines'))
        fig.update_layout(
            title=f'Line Chart: {y_axis} vs {x_axis}',
            xaxis=dict(title=x_axis),
            yaxis=dict(title=y_axis)
        )

        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)

    if 'heatmap_button' in request.form:
        # Generate heatmap using Plotly Express
        fig = px.imshow(df.set_index([x_axis, y_axis]))
        fig.update_xaxes(title=x_axis)
        fig.update_yaxes(title=y_axis)
        fig.update_layout(title='Heatmap')

        graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('visualise.html', plot_div=graph, columns=columns, x_selected=x_axis, y_selected=y_axis)



    return render_template('visualise.html', columns=columns)
    
    
    
        
    
UPLOAD_FOLDER = '/var/www/html/PhenoPhene/manhattan'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/manhattan', methods=['GET', 'POST'])
def manhattan():
    plot_url = None
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            # Save uploaded CSV file
            csv_file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(csv_file_path)
            
            # Generate hoverable Manhattan plot
            generate_hoverable_manhattan_plot(csv_file_path)
            
            # Encode the generated image to base64
            with open('manhattan_plot.png', 'rb') as img_file:
                plot_url = base64.b64encode(img_file.read()).decode()

    return render_template('visualise.html', plot_url=plot_url)

@app.route('/var/www/html/PhenoPhene/manhattan/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def generate_hoverable_manhattan_plot(csv_file_path):
    # Read CSV file
    df = pd.read_csv(csv_file_path, sep=',')
    
    # -log_10(pvalue)
    df['minuslog10pvalue'] = -np.log10(df['P'])
    df['CHR'] = df['CHR'].astype('category')
    df = df.sort_values('CHR')
    
    # How to plot gene vs. -log10(pvalue) and colour it by chromosome?
    df['ind'] = range(len(df))
    df_grouped = df.groupby('CHR')
    
    # Set custom style for plot size
    plt.style.use({'figure.figsize': (10, 6)})
    
    # Manhattan plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = ['darkred', 'darkgreen', 'darkblue', 'gold']
    x_labels = []
    x_labels_pos = []
    scatter_plots = []
    for num, (name, group) in enumerate(df_grouped):
        scatter = ax.scatter(group['ind'], group['minuslog10pvalue'], color=colors[num % len(colors)])
        scatter_plots.append(scatter)
        x_labels.append(name)
        x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0]) / 2))
    
    ax.set_xticks(x_labels_pos)
    ax.set_xticklabels(x_labels)
    ax.set_xlim([0, len(df)])
    ax.set_ylim([0, 3.5])
    ax.set_xlabel('Chromosome')
    
    # Add hoverable labels
    mplcursors.cursor(scatter_plots, hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"CHR: {df.iloc[sel.target.index]['CHR']}\nminuslog10pvalue: {df.iloc[sel.target.index]['minuslog10pvalue']:.2f}"
    ))

    # Save hoverable plot to a PNG image
    plt.savefig(os.path.join('/var/www/html/PhenoPhene/static', 'manhattan_plot.png'), format='png')
    plt.close() 



if __name__ == '__main__':
    app.run(debug=True)
