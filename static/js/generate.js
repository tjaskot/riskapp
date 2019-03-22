// Enter a speed between 0 and 180
var level = 125;

// Trig to calc meter point
var degrees = 180 - level,
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

var data = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 28, color:'rgba(0, 100, 200, 1)'},
    showlegend: true,
    name: 'Schedule Integer (Interactive values below)',
    text: level,
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

var layout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: 'rgba(0, 100, 200, 0.5)',
      line: {
        color: 'rgba(0, 100, 200, 0.5)'
      }
    }],
  title: '<b>Schedule</b> <br> Scale 0-5',
  height: 600,
  width: 900,
  xaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};

Plotly.newPlot('schedulePlotChart', data, layout, {showSendToCloud:true});
