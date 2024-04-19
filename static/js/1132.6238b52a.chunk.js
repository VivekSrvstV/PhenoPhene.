"use strict";(self.webpackChunk_jbrowse_web=self.webpackChunk_jbrowse_web||[]).push([[1132],{20706:function(e,t,r){r.d(t,{s:function(){return a}});var o=r(96902),n=o.createContext({});function a(){return o.useContext(n)}t.Z=n},51132:function(e,t,r){r.r(t),r.d(t,{default:function(){return L},getStepButtonUtilityClass:function(){return x},stepButtonClasses:function(){return h}});var o=r(56666),n=r(31461),a=r(7896),i=r(96902),l=r(24463),c=r(73674),s=r(2252),u=r(53068),p=r(83413),d=r(15817),v=r(3785),f=r(29736),Z=r(20706),m=r(74732),b=r(61235);function x(e){return(0,b.Z)("MuiStepButton",e)}var h=(0,m.Z)("MuiStepButton",["root","horizontal","vertical","touchRipple"]),S=r(29938),C=["children","className","icon","optional"],y=(0,s.ZP)(p.Z,{name:"MuiStepButton",slot:"Root",overridesResolver:function(e,t){var r=e.ownerState;return[(0,o.Z)({},"& .".concat(h.touchRipple),t.touchRipple),t.root,t[r.orientation]]}})((function(e){var t=e.ownerState;return(0,a.Z)({width:"100%",padding:"24px 16px",margin:"-24px -16px",boxSizing:"content-box"},"vertical"===t.orientation&&{justifyContent:"flex-start",padding:"8px",margin:"-8px"},(0,o.Z)({},"& .".concat(h.touchRipple),{color:"rgba(0, 0, 0, 0.3)"}))})),L=i.forwardRef((function(e,t){var r=(0,u.Z)({props:e,name:"MuiStepButton"}),o=r.children,s=r.className,p=r.icon,m=r.optional,b=(0,n.Z)(r,C),h=i.useContext(Z.Z),L=h.disabled,w=h.active,R=i.useContext(f.Z).orientation,g=(0,a.Z)({},r,{orientation:R}),M=function(e){var t=e.classes,r={root:["root",e.orientation],touchRipple:["touchRipple"]};return(0,c.Z)(r,x,t)}(g),N={icon:p,optional:m},j=(0,v.Z)(o,["StepLabel"])?i.cloneElement(o,N):(0,S.jsx)(d.Z,(0,a.Z)({},N,{children:o}));return(0,S.jsx)(y,(0,a.Z)({focusRipple:!0,disabled:L,TouchRippleProps:{className:M.touchRipple},className:(0,l.default)(M.root,s),ref:t,ownerState:g,"aria-current":w?"step":void 0},b,{children:j}))}))},72834:function(e,t,r){r.d(t,{Z:function(){return C}});var o,n=r(56666),a=r(7896),i=r(31461),l=r(96902),c=r(24463),s=r(73674),u=r(2252),p=r(53068),d=r(30992),v=r(29938),f=(0,d.Z)((0,v.jsx)("path",{d:"M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm-2 17l-5-5 1.4-1.4 3.6 3.6 7.6-7.6L19 8l-9 9z"}),"CheckCircle"),Z=(0,d.Z)((0,v.jsx)("path",{d:"M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"}),"Warning"),m=r(66026),b=r(40166),x=["active","className","completed","error","icon"],h=(0,u.ZP)(m.Z,{name:"MuiStepIcon",slot:"Root",overridesResolver:function(e,t){return t.root}})((function(e){var t,r=e.theme;return t={display:"block",transition:r.transitions.create("color",{duration:r.transitions.duration.shortest}),color:(r.vars||r).palette.text.disabled},(0,n.Z)(t,"&.".concat(b.Z.completed),{color:(r.vars||r).palette.primary.main}),(0,n.Z)(t,"&.".concat(b.Z.active),{color:(r.vars||r).palette.primary.main}),(0,n.Z)(t,"&.".concat(b.Z.error),{color:(r.vars||r).palette.error.main}),t})),S=(0,u.ZP)("text",{name:"MuiStepIcon",slot:"Text",overridesResolver:function(e,t){return t.text}})((function(e){var t=e.theme;return{fill:(t.vars||t).palette.primary.contrastText,fontSize:t.typography.caption.fontSize,fontFamily:t.typography.fontFamily}})),C=l.forwardRef((function(e,t){var r=(0,p.Z)({props:e,name:"MuiStepIcon"}),n=r.active,l=void 0!==n&&n,u=r.className,d=r.completed,m=void 0!==d&&d,C=r.error,y=void 0!==C&&C,L=r.icon,w=(0,i.Z)(r,x),R=(0,a.Z)({},r,{active:l,completed:m,error:y}),g=function(e){var t=e.classes,r={root:["root",e.active&&"active",e.completed&&"completed",e.error&&"error"],text:["text"]};return(0,s.Z)(r,b.M,t)}(R);if("number"===typeof L||"string"===typeof L){var M=(0,c.default)(u,g.root);return y?(0,v.jsx)(h,(0,a.Z)({as:Z,className:M,ref:t,ownerState:R},w)):m?(0,v.jsx)(h,(0,a.Z)({as:f,className:M,ref:t,ownerState:R},w)):(0,v.jsxs)(h,(0,a.Z)({className:M,ref:t,ownerState:R},w,{children:[o||(o=(0,v.jsx)("circle",{cx:"12",cy:"12",r:"12"})),(0,v.jsx)(S,{className:g.text,x:"12",y:"12",textAnchor:"middle",dominantBaseline:"central",ownerState:R,children:L})]}))}return L}))},40166:function(e,t,r){r.d(t,{M:function(){return a}});var o=r(74732),n=r(61235);function a(e){return(0,n.Z)("MuiStepIcon",e)}var i=(0,o.Z)("MuiStepIcon",["root","active","completed","error","text"]);t.Z=i},15817:function(e,t,r){var o=r(56666),n=r(31461),a=r(7896),i=r(96902),l=r(24463),c=r(73674),s=r(2252),u=r(53068),p=r(72834),d=r(29736),v=r(20706),f=r(64282),Z=r(29938),m=["children","className","componentsProps","error","icon","optional","slotProps","StepIconComponent","StepIconProps"],b=(0,s.ZP)("span",{name:"MuiStepLabel",slot:"Root",overridesResolver:function(e,t){var r=e.ownerState;return[t.root,t[r.orientation]]}})((function(e){var t,r=e.ownerState;return(0,a.Z)((t={display:"flex",alignItems:"center"},(0,o.Z)(t,"&.".concat(f.Z.alternativeLabel),{flexDirection:"column"}),(0,o.Z)(t,"&.".concat(f.Z.disabled),{cursor:"default"}),t),"vertical"===r.orientation&&{textAlign:"left",padding:"8px 0"})})),x=(0,s.ZP)("span",{name:"MuiStepLabel",slot:"Label",overridesResolver:function(e,t){return t.label}})((function(e){var t,r=e.theme;return(0,a.Z)({},r.typography.body2,(t={display:"block",transition:r.transitions.create("color",{duration:r.transitions.duration.shortest})},(0,o.Z)(t,"&.".concat(f.Z.active),{color:(r.vars||r).palette.text.primary,fontWeight:500}),(0,o.Z)(t,"&.".concat(f.Z.completed),{color:(r.vars||r).palette.text.primary,fontWeight:500}),(0,o.Z)(t,"&.".concat(f.Z.alternativeLabel),{marginTop:16}),(0,o.Z)(t,"&.".concat(f.Z.error),{color:(r.vars||r).palette.error.main}),t))})),h=(0,s.ZP)("span",{name:"MuiStepLabel",slot:"IconContainer",overridesResolver:function(e,t){return t.iconContainer}})((function(){return(0,o.Z)({flexShrink:0,display:"flex",paddingRight:8},"&.".concat(f.Z.alternativeLabel),{paddingRight:0})})),S=(0,s.ZP)("span",{name:"MuiStepLabel",slot:"LabelContainer",overridesResolver:function(e,t){return t.labelContainer}})((function(e){var t=e.theme;return(0,o.Z)({width:"100%",color:(t.vars||t).palette.text.secondary},"&.".concat(f.Z.alternativeLabel),{textAlign:"center"})})),C=i.forwardRef((function(e,t){var r,o=(0,u.Z)({props:e,name:"MuiStepLabel"}),s=o.children,C=o.className,y=o.componentsProps,L=void 0===y?{}:y,w=o.error,R=void 0!==w&&w,g=o.icon,M=o.optional,N=o.slotProps,j=void 0===N?{}:N,P=o.StepIconComponent,I=o.StepIconProps,z=(0,n.Z)(o,m),k=i.useContext(d.Z),B=k.alternativeLabel,T=k.orientation,_=i.useContext(v.Z),A=_.active,W=_.disabled,F=_.completed,H=_.icon,D=g||H,E=P;D&&!E&&(E=p.Z);var U=(0,a.Z)({},o,{active:A,alternativeLabel:B,completed:F,disabled:W,error:R,orientation:T}),q=function(e){var t=e.classes,r=e.orientation,o=e.active,n=e.completed,a=e.error,i=e.disabled,l=e.alternativeLabel,s={root:["root",r,a&&"error",i&&"disabled",l&&"alternativeLabel"],label:["label",o&&"active",n&&"completed",a&&"error",i&&"disabled",l&&"alternativeLabel"],iconContainer:["iconContainer",o&&"active",n&&"completed",a&&"error",i&&"disabled",l&&"alternativeLabel"],labelContainer:["labelContainer",l&&"alternativeLabel"]};return(0,c.Z)(s,f.H,t)}(U),G=null!=(r=j.label)?r:L.label;return(0,Z.jsxs)(b,(0,a.Z)({className:(0,l.default)(q.root,C),ref:t,ownerState:U},z,{children:[D||E?(0,Z.jsx)(h,{className:q.iconContainer,ownerState:U,children:(0,Z.jsx)(E,(0,a.Z)({completed:F,active:A,error:R,icon:D},I))}):null,(0,Z.jsxs)(S,{className:q.labelContainer,ownerState:U,children:[s?(0,Z.jsx)(x,(0,a.Z)({ownerState:U},G,{className:(0,l.default)(q.label,null==G?void 0:G.className),children:s})):null,M]})]}))}));C.muiName="StepLabel",t.Z=C},64282:function(e,t,r){r.d(t,{H:function(){return a}});var o=r(74732),n=r(61235);function a(e){return(0,n.Z)("MuiStepLabel",e)}var i=(0,o.Z)("MuiStepLabel",["root","horizontal","vertical","label","active","completed","error","disabled","iconContainer","alternativeLabel","labelContainer"]);t.Z=i},29736:function(e,t,r){r.d(t,{s:function(){return a}});var o=r(96902),n=o.createContext({});function a(){return o.useContext(n)}t.Z=n}}]);
//# sourceMappingURL=1132.6238b52a.chunk.js.map