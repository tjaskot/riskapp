// ----------------------------------------------------------------------
// Schedule Variable Inputs
schedVar1 = 20;
schedVar2 = 20;
schedVar3 = 20;
schedVar4 = 20;
schedVar5 = 20;

// Total variable in schedule
var schedLevel = schedVar1 + schedVar2 + schedVar3 + schedVar4 + schedVar5;

// Trig to calc meter point
var degrees = 180 - schedLevel,
     radius = .5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

// Path: may have to change to create a better triangle
// Center pointer marker
var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);

var schedData = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 20, color:'rgba(0, 100, 200, 1)'},
    showlegend: true,
    name: 'Schedule Value',
    text: schedLevel,
    hoverinfo: 'text+name'},
  //Change these value to adjust chart circumference.
  { values: [50/6, 50/6, 50/6, 50/6, 50/6, 50/6, 50],
  rotation: 90,
  text: ['Great', 'Very Good', 'Good', 'Fair',
            'Poor', 'Very Poor', ''],
  textinfo: 'text',
  textposition:'inside',
  marker: {colors:['rgba(0, 210, 0, .8)', 'rgba(0, 200, 0, .5)',
                         'rgba(0, 195, 0, .2)', 'rgba(195, 0, 0, .25)',
                         'rgba(200, 0, 0, .5)', 'rgba(210, 0, 0, .8)',
                         'rgba(255, 255, 255, 0)']},
  labels: ['WayAhead', 'Ahead', 'OnTime', 'JustBehind', 'Behind', 'FarBehind', 'Full-Circle'],
  hoverinfo: 'label',
  hole: .5,
  type: 'pie',
  showlegend: true
}];

var schedLayout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: 'rgba(0, 100, 200, 0.5)',
      line: {
        color: 'rgba(0, 100, 200, 0.5)'
      }
    }],
  title: '<b>Schedule</b> <br> Scale 0-5',
  // Height & Width replaced here with css values (userPlotlyChart) for reactive experience
  xaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};

// ----------------------------------------------------------------------
// Risk Variable Inputs
riskVar1 = 25;
riskVar2 = 25;
riskVar3 = 25;
riskVar4 = 25;
riskVar5 = 25;

// Total variable in schedule
var riskLevel = riskVar1 + riskVar2 + riskVar3 + riskVar4 + riskVar5;

// Trig to calc meter point
var degrees = 180 - riskLevel,
     radius = .5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

// Path: may have to change to create a better triangle
// Center pointer marker
var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);

var riskData = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 20, color:'rgba(0, 100, 200, 1)'},
    showlegend: true,
    name: 'Risk Value',
    text: riskLevel,
    hoverinfo: 'text+name'},
  //Change these value to adjust chart circumference.
  { values: [50/6, 50/6, 50/6, 50/6, 50/6, 50/6, 50],
  rotation: 90,
  text: ['Great', 'Very Good', 'Good', 'Fair',
            'Poor', 'Very Poor', ''],
  textinfo: 'text',
  textposition:'inside',
  marker: {colors:['rgba(0, 210, 0, .8)', 'rgba(0, 200, 0, .5)',
                         'rgba(0, 195, 0, .2)', 'rgba(195, 0, 0, .25)',
                         'rgba(200, 0, 0, .5)', 'rgba(210, 0, 0, .8)',
                         'rgba(255, 255, 255, 0)']},
  labels: ['WayAhead', 'Ahead', 'OnTime', 'JustBehind', 'Behind', 'FarBehind', 'Full-Circle'],
  hoverinfo: 'label',
  hole: .5,
  type: 'pie',
  showlegend: true
}];

var riskLayout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: 'rgba(0, 100, 200, 0.5)',
      line: {
        color: 'rgba(0, 100, 200, 0.5)'
      }
    }],
  title: '<b>Risk</b> <br> Scale 0-5',
  // Height & Width replaced here with css values (userPlotlyChart) for reactive experience
  xaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
// Cost Variable Inputs
costVar1 = 30;
costVar2 = 30;
costVar3 = 30;
costVar4 = 30;
costVar5 = 30;

// Total variable in schedule
var costLevel = costVar1 + costVar2 + costVar3 + costVar4 + costVar5;

// Trig to calc meter point
var degrees = 180 - costLevel,
     radius = .5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

// Path: may have to change to create a better triangle
// Center pointer marker
var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);

var costData = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 20, color:'rgba(0, 100, 200, 1)'},
    showlegend: true,
    name: 'Cost Value',
    text: costLevel,
    hoverinfo: 'text+name'},
  //Change these value to adjust chart circumference.
  { values: [50/6, 50/6, 50/6, 50/6, 50/6, 50/6, 50],
  rotation: 90,
  text: ['Great', 'Very Good', 'Good', 'Fair',
            'Poor', 'Very Poor', ''],
  textinfo: 'text',
  textposition:'inside',
  marker: {colors:['rgba(0, 210, 0, .8)', 'rgba(0, 200, 0, .5)',
                         'rgba(0, 195, 0, .2)', 'rgba(195, 0, 0, .25)',
                         'rgba(200, 0, 0, .5)', 'rgba(210, 0, 0, .8)',
                         'rgba(255, 255, 255, 0)']},
  labels: ['WayAhead', 'Ahead', 'OnTime', 'JustBehind', 'Behind', 'FarBehind', 'Full-Circle'],
  hoverinfo: 'label',
  hole: .5,
  type: 'pie',
  showlegend: true
}];

var costLayout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: 'rgba(0, 100, 200, 0.5)',
      line: {
        color: 'rgba(0, 100, 200, 0.5)'
      }
    }],
  title: '<b>Cost</b> <br> Scale 0-5',
  // Height & Width replaced here with css values (userPlotlyChart) for reactive experience
  xaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};
// ----------------------------------------------------------------------

// Schedule Plot
Plotly.newPlot('schedulePlotChart', schedData, schedLayout, {showSendToCloud:true});
// Risk Plot
Plotly.newPlot('riskPlotChart', riskData, riskLayout, {showSendToCloud:true});
// Cost Plot
Plotly.newPlot('costPlotChart', costData, costLayout, {showSendToCloud:true});
