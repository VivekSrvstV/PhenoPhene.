"use strict";(self.webpackChunk_jbrowse_web=self.webpackChunk_jbrowse_web||[]).push([[3499],{23499:function(t,e,n){n.r(e),n.d(e,{default:function(){return d}});var r=n(33028),a=n(96234),u=n(32723),s=n(34795),c=n(9249),o=n(87371),i=n(45754),f=n(13820),p=n(2646),l=n(32145),h=n(95802),m=n(93824),v=n(44922),d=function(t){(0,i.Z)(n,t);var e=(0,f.Z)(n);function n(){var t;(0,c.Z)(this,n);for(var r=arguments.length,a=new Array(r),u=0;u<r;u++)a[u]=arguments[u];return(t=e.call.apply(e,[this].concat(a))).setupP=void 0,t}return(0,o.Z)(n,[{key:"setup",value:function(){var t=(0,s.Z)((0,u.Z)().mark((function t(e){var n=this;return(0,u.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return this.setupP||(this.setupP=this.setupPre(e).catch((function(t){throw n.setupP=void 0,t}))),t.abrupt("return",this.setupP);case 2:case"end":return t.stop()}}),t,this)})));return function(e){return t.apply(this,arguments)}}()},{key:"setupPre",value:function(){var t=(0,s.Z)((0,u.Z)().mark((function t(e){var n,r,s,c,o,i,f,p,h,m,d,Z,w;return(0,u.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n=this.getConf("assemblyNames"),r=this.pluginManager,s=(0,l.openLocation)(this.getConf("bed1Location"),r),c=(0,l.openLocation)(this.getConf("bed2Location"),r),o=(0,l.openLocation)(this.getConf("mcscanAnchorsLocation"),r),t.next=7,Promise.all([s,c,o].map((function(t){return(0,v.pJ)(t,e)})));case 7:return i=t.sent,f=(0,a.Z)(i,3),p=f[0],h=f[1],m=f[2],d=(0,v.SN)(p),Z=(0,v.SN)(h),w=m.split(/\n|\r\n|\r/).filter((function(t){return!!t&&"###"!==t})).map((function(t,e){var n=t.split("\t"),r=(0,a.Z)(n,3),u=r[0],s=r[1],c=r[2],o=d.get(u),i=Z.get(s);if(!o||!i)throw new Error("feature not found, ".concat(u," ").concat(s," ").concat(o," ").concat(i));return[o,i,+c,e]})),t.abrupt("return",{assemblyNames:n,feats:w});case 16:case"end":return t.stop()}}),t,this)})));return function(e){return t.apply(this,arguments)}}()},{key:"hasDataForRefName",value:function(){var t=(0,s.Z)((0,u.Z)().mark((function t(){return(0,u.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",!0);case 1:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}()},{key:"getRefNames",value:function(){var t=(0,s.Z)((0,u.Z)().mark((function t(){return(0,u.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",[]);case 1:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}()},{key:"getFeatures",value:function(t){var e=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return(0,m.ObservableCreate)(function(){var c=(0,s.Z)((0,u.Z)().mark((function s(c){var o,i,f,p,l;return(0,u.Z)().wrap((function(u){for(;;)switch(u.prev=u.next){case 0:return u.next=2,e.setup(n);case 2:o=u.sent,i=o.assemblyNames,f=o.feats,-1!==(p=i.indexOf(t.assemblyName))&&(l=0===p,f.forEach((function(e){var n=(0,a.Z)(e,4),u=n[0],s=n[1],o=n[2],f=n[3],m=l?[u,s]:[s,u],v=(0,a.Z)(m,2),d=v[0],Z=v[1];d.refName===t.refName&&(0,h.doesIntersect2)(t.start,t.end,d.start,d.end)&&c.next(new h.SimpleFeature((0,r.Z)((0,r.Z)({},d),{},{uniqueId:"".concat(p,"-").concat(f),syntenyId:f,strand:d.strand*Z.strand,assemblyName:i[+!l],score:o,mate:(0,r.Z)((0,r.Z)({},Z),{},{assemblyName:i[+l]})})))}))),c.complete();case 8:case"end":return u.stop()}}),s)})));return function(t){return c.apply(this,arguments)}}())}},{key:"freeResources",value:function(){}}]),n}(p.BaseFeatureDataAdapter);d.capabilities=["getFeatures","getRefNames"]},44922:function(t,e,n){n.d(e,{$R:function(){return p},SN:function(){return o},lq:function(){return c},pJ:function(){return i}});var r=n(32723),a=n(34795),u=n(96234),s=n(16959);function c(t){return 31===t[0]&&139===t[1]&&8===t[2]}function o(t){return new Map(t.split(/\n|\r\n|\r/).filter((function(t){return!!t||t.startsWith("#")})).map((function(t){var e=t.split("\t"),n=(0,u.Z)(e,6),r=n[0],a=n[1],s=n[2],c=n[3];return[c,{refName:r,start:+a,end:+s,score:+n[4],name:c,strand:"-"===n[5]?-1:1}]})))}function i(t,e){return f.apply(this,arguments)}function f(){return(f=(0,a.Z)((0,r.Z)().mark((function t(e,n){var a;return(0,r.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.readFile(n);case 2:if(a=t.sent,t.t0=new TextDecoder("utf8",{fatal:!0}),!c(a)){t.next=10;break}return t.next=7,(0,s.unzip)(a);case 7:t.t1=t.sent,t.next=11;break;case 10:t.t1=a;case 11:return t.t2=t.t1,t.abrupt("return",t.t0.decode.call(t.t0,t.t2));case 13:case"end":return t.stop()}}),t)})))).apply(this,arguments)}function p(t,e){return t.map((function(t,n){return[t,e[n]]}))}}}]);
//# sourceMappingURL=3499.c02d0142.chunk.js.map