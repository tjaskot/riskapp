//This section can be moved to the python portion of the code if either you want to use ajax post to a url or don't need to leverage the visual. The python code for /generatesomethingelse is commented out in riskapp.py.
/* Ajax call:
 * $.ajax({
 *     type: "POST",
 *     url: /generatesomethingelse,
 *     data: {variable:variable}
 *     success: function(data, 200),
 *     error: function(unknown, 400)
 * })
 */

//This is used in tandem with the css to make the plotly charts and design reactive to the window height and width.
var ww = window.innerWidth;
var wh = window.innerHeight;
if (ww < 600) {
	chartW = ww;
	chartH = wh * 0.85;
} else if (ww >= 600 && ww < 800) {
	chartW = 600;
	chartH = 500;
} else {
	chartW = 800;
	chartH = 650;
}

//*********Chart variables**********//
//-----------------------------------------------
//Variables are instantiated here so browser does not read null and functions don't error out. Error handling is internal to each section of chart data.
// Schedule Variable input for Schedule chart
var schedLevel;
// Risk Variable input for Rish chart
var riskLevel;
// Cost Variable input for Cost chart
var costLevel;
//----------------------------------------------

function genChartData() {
        //Variable instantiation so functions do not error out, and keep internal to function call so no stashed variable become out of scope when clicking buttons on webpage.
        //Median Salaries per hour for each genre of employee, given to us from customer
        var medStw = 67000;
        var medSpm = 210000;
        var medSjd = 88000;
        var medSjt = 88000;
        var medSsd = 185000;
        var medSst = 185000;
        //Total number of sprint hours dedicated to release, 2.5% of 40 hour work week
        var relHrs = 2;
        //Total number of hours dedicated by Developer Scrum team to Agile Ceremonies plus PBR. This value is 16 as defined by Agile documentation
        var totAgileHrs = 16;

	//These variables will be used in the algorithm that determines the values to be passed into each plotly chart. The project left out the "var" instantiation for each value because without that instantiation, this function is directly translatable to python code, should you want to movethis to the python file instead of housing it here in javascript.
	//Variables pulled from html user input:
	weeksLong = document.getElementById('weeksLong').value;
	totEpics = document.getElementById('totEpics').value;
	sprintWeek = document.getElementById('sprintWeek').value;
	storyPoint = document.getElementById('storyPoint').value;
	techWriterValue = document.getElementById('techWriter').value;
	prodManValue = document.getElementById('prodMan').value;
	jrDevValue = document.getElementById('jrDev').value;
	jrTestValue = document.getElementById('jrTest').value;
	srDevValue = document.getElementById('srDev').value;
	srTestValue = document.getElementById('srTest').value;

	//NEED to turn the variables into numbers if they are not, some browsers turn numbers into strings if the character count is more than one. Example, 1 is a number, 15 is a string.
        weeksLong = Number(weeksLong);
        totEpics = Number(totEpics);
        sprintWeek = Number(sprintWeek);
        storyPoint = Number(storyPoint);
        techWriterValue = Number(techWriterValue);
        prodManValue = Number(prodManValue);
        jrDevValue = Number(jrDevValue);
        jrTestValue = Number(jrTestValue);
        srDevValue = Number(srDevValue);
        srTestValue = Number(srTestValue);

        //Instantiate the value for average stories so that the algirithm doesn't error out.
        avgStory = storyPoint / totEpics;

	//Convert the percentage values to decimals for mathematical computation
	techWriter = techWriterValue / 100;
	prodMan = prodManValue / 100;
	jrDev = jrDevValue / 100;
	jrTest = jrTestValue / 100;
	srDev = srDevValue / 100;
	srTest = srTestValue / 100;

	//Total number of sprints per contract
	totSprints = weeksLong / sprintWeek;

	//Total average number of stories per sprint
	//This table definition was defined by the project as it relates to the customer information. If you look at the else statement at the end of this condition, then you will see a guesitmated number of stories per epic. From this guestimation you can correlate your information and pass the value directly into the algorithm.
 	if (storyPoint > 0 && storyPoint < 100) {
		avgStory = 7;
	} else if (storyPoint >= 100 && storyPoint < 250) {
		avgStory = 8;
	} else if (storyPoint >= 250 && storyPoint < 400) {
		avgStory = 9;
	} else if (storyPoint >= 400 && storyPoint < 500) {
		avgStory = 10;
	} else if (storyPoint >= 500 && storyPoint < 650) {
		avgStory = 11;
	} else if (storyPoint >= 650 && storyPoint < 775) {
		avgStory = 12;
	} else if (storyPoint >= 775 && storyPoint < 900) {
		avgStory = 13;
	} else if (storyPoint >= 900 && storyPoint < 1000) {
		avgStory = 14;
	} else if (storyPoint >= 1000 && storyPoint < 1100) {
		avgStory = 15;
	} else if (storyPoint >= 1100 && storyPoint < 1250) {
		avgStory = 16;
	} else if (storyPoint >= 1250 && storyPoint < 1375) {
		avgStory = 17;
	} else if (storyPoint >= 1375 && storyPoint < 1500) {
		avgStory = 18;
	} else {
		avgStory = storyPoint / totEpics;
	}

	//Total average number of stories per epic
	avgEpicStory = (totSprints * avgStory) / totEpics;

	//Variables created from inputs and mandated values, work rate is the percent of agile effort, multiplied by cost, associated to each median salary, and allocated per sprint:
        //Story Point value as defined by user, no need to recreate variable, unless posting it with another name to a python method for another database value, or for another reason you can develop :)
	//Cost Contribution Tech Writer
	cCtw = storyPoint * techWriter;
	//Cost Contribution Product Manager
	cCpm = storyPoint * prodMan;
	//Cost Contribution Junior Dev
	cCjd = storyPoint * jrDev;
	//Cost Contribution Junior Tester
	cCjt = storyPoint * jrTest;
	//Cost Contribution Senior Dev
	cCsd = storyPoint * srDev;
	//Cost Contribution Senior Tester
	cCst = storyPoint * srTest;

        //Work Rate for a Tech Writer, cost contribution per sprint
        workRatetw = (cCtw / sprintWeek) * medStw;
        //Work Rate for a Product Manager, cost contribution per sprint
        workRatepm = (cCpm / sprintWeek) * medSpm;
        //Work Rate for a Junior Developer, cost contribution per sprint
        workRatejd = (cCjd / sprintWeek) * medSjd;
        //Work Rate for a Junior Tester, cost contribution per sprint
        workRatejt = (cCjt/ sprintWeek) * medSjt;
        //Work Rate for a Senior Developer, cost contribution per sprint
        workRatesd = (cCsd / sprintWeek) * medSsd;
        //Work Rate for a Senior Tester, cost contribution per sprint
        workRatest = (cCst / sprintWeek) * medSst;

	//The amount of hours each person will do is produced by hoursLong an computed here for complete monetary cost.
	hoursLong = weeksLong * 40;
        //Total Fiscal Cost for a Tech Writer
        totWorkCosttw = (medStw / 365 * hoursLong) * techWriter;
        //Total Fiscal Cost for a Product Manager
        totWorkCostpm = (medSpm / 365 * hoursLong) * prodMan;
        //Total Fiscal Cost for a Junior Developer
        totWorkCostjd = (medSjd / 365 * hoursLong) * jrDev;
        //Total Fiscal Cost for a Junior Tester
        totWorkCostjt = (medSjt / 365 * hoursLong) * jrTest;
        //Total Fiscal Cost for a Senior Developer
        totWorkCostsd = (medSsd / 365 * hoursLong) * srDev;
        //Total Fiscal Cost for a Senior Tester
        totWorkCostst = (medSst / 365 * hoursLong) * srTest;

        //Cost per Epic: story point multiplied by stories and divided into epics
	//  - number of stories by each individual
        costCycletw = (storyPoint * totEpics) / (workRatetw);
        costCyclepm = (storyPoint * totEpics) / (workRatepm);
        costCyclejd = (storyPoint * totEpics) / (workRatejd);
        costCyclejt = (storyPoint * totEpics) / (workRatejt);
        costCyclesd = (storyPoint * totEpics) / (workRatesd);
        costCyclest = (storyPoint * totEpics) / (workRatest);

        //Created the weighted valued for the under budget best case scenario, and over budget worst case scenario. Weighted values for each work rate are below for under and over budget prediction:
	//Weighted Under budget Cycle Cost for each grouping
	wCycletw = costCycletw * 0.95;
	wCyclepm = costCyclepm * 0.95;
	wCyclejd = costCyclejd * 0.70;
        wCyclejt = costCyclejt * 0.80;
        wCyclesd = costCyclesd * 0.85;
	wCyclest = costCyclest * 0.90;

	//Weighted Over budget Cycle Cost for each grouping
	wCycletw = costCycletw * 1.05;
	wCyclepm = costCyclepm * 1.05;
	wCyclejd = costCyclejd * 1.3;
        wCyclejt = costCyclejt * 1.2;
        wCyclesd = costCyclesd * 1.15;
	wCyclest = costCyclest * 1.1;

	//This variable is the total work allowed for a sprint with the input percentages of agile effort allowed per indidivual category group (tw, pm, jr, st, etc...).
	//  - The amount of points per sprint that is allocated for release is converted in this equation
        totWorkHrs = (weeksLong / sprintWeek) - (totAgileHrs + relHrs);
	totWorkPoints = totWorkHrs * storyPoint;
	
        //#######################################################
	//Setting values for final chart input and this will create the level set of complexity for the respective areas. As cost does not vary because time is a dependant variable of cost, it will not be included in the story point complexity level setting.
	
	//Instantiate variable to reset value if data is requested multiple times.
	var riskFinal;
	var schedFinal;
	//Reason we divide the sprintWeek by two is to baseline sprint iterations off 2 weeks, as 2 weeks is most recommended by agile documentation. Anything more than that and this equation will accomodate for less efficiency in sprint week patterns.
	storyToRisk = storyPoint / weeksLong / (sprintWeek / 2);
	//Story point generals are given in this conditional set of statements. This is just to level set the risk value for complexity. It will be further manipulated below.
	if (storyToRisk <= 125) {
		riskFinal = 180;
		schedFinal = 125;
	} else if (storyToRisk > 125 && storyToRisk <= 175) {
		riskFinal = 165;
                schedFinal = 105;
	} else {
	        riskFinal = 145;
                schedFinal = 85;
        }

	//Set Cost value final
	//-------------------
	//Cost is straight forward, linear in nature and taken from the industry standard for a median salary. Compilation will be created from simple mathematic concepts seen below, where the total cost is for the given number of days the employees work.
	//-------------------
	
	//Instantiating costFinal in case data is requested multiple times in browser.
	var costFinal;

        costFinal = totWorkCosttw + totWorkCostpm + totWorkCostjd + totWorkCostjt + totWorkCostsd + totWorkCostst; 
	//This step correlates the value of cost from thousand into the chart value of 1 - 180. Take the average of all median salaries and then above and below that average correlates to the english terms of poor, fair, good, very good.
 	//  - With the given dataset, the average cost of contract per 2 week sprint is 27000. We will calculate this per week of work, can be caluclated with sprint information if user prefers to change data. Sometimes monetary values are official use only and as such this program will use industry mean salaries.
	var costRelate;
	costRelate = 13500 / (costFinal / weeksLong);
	if (costRelate <= 0.5) {
		costFinalChart = 15;
	} else if (costRelate > 0.5 && costRelate < 0.65) {
		costFinalChart = 45;
	} else if (costRelate >= 0.65 && costRelate <= 0.9) {
		costFinalChart = 75;
	} else if (costRelate > 0.9 && costRelate < 1.05) {
		costFinalChart = 115;
	} else if (costRelate >= 1.05 && costRelate < 1.25) {
		costFinalChart = 145;
	} else {
		costFinalChart = 170;
	}
	//Rounding to two decimal places
	costFinalRound = costFinal.toFixed(2);
	//Debugging purposes
	//console.log("This is the total cost it will be for the project: " + costFinalRound);


	//Set Risk value final
	//--------------------
	//  - This value will be subtracted from 180 because the higher the risk the lower the value...in other words we start with no risk at 180 and go down from there. Whereas, the other values are additive. 
	//  - The success percentages were defined by correlating integer values to the respective english phrases. For example the input for tech writer "What is the percentage of effor your Tech Writer..." is interpolated as integer success value of 95%. This was a project decision, as writing documents has litle failure. This logic applies to all of the input enligh phrases which correlate to integer values.
	//--------------------
	
	//  - Each individual group gets a weighted 30 points allocated to it because there are 6 groups total and with there being 180 degrees in a dial chart 180/6 is equal to 30. The weighted values are produced from the baseline data set. Since everything is based off 1 story point, we will use 1 as the weighting scale. Obtained the decimal values with 1/<weight_percentage>. Example: 1/0.95, or 1/0.70.
	//As the tech writer is documents each and all items associated with the development of the scrum team, there is little risk inherited
	if (techWriterValue <= 5) {
		riskFinal = riskFinal * 0.95;
	} else if (techWriterValue > 5 && techWriterValue < 30) {
		riskFinal = riskFinal * 1.05;
	} else {
		riskFinal = riskFinal * 1.25;
	}
	//If the product manager needs to spend more than 40%, then the product is extremely complex and needs to refined in scope
	if (prodManValue <= 10) {
		riskFinal = riskFinal * 0.98;
	} else if (prodManValue > 10 && prodManValue <= 20) {
		riskFinal = riskFinal * 0.95;
	} else if (prodManValue >= 10 && prodManValue <= 20) {
		riskFinal = riskFinal * 0.875;
	} else if (prodManValue > 20 && prodManValue <= 40) {
		riskFinal = riskFinal * 0.825;
	} else {
		riskFinal = riskFinal * 0.75;
	}
        //As junior developer put more time into a project, that project becomes more complex. Therefore the returns are diminishing as more time is put into project.
	if (jrDevValue <= 15) {
		riskFinal = riskFinal * 0.95;
	} else if (jrDevValue > 15 && jrDevValue < 25) {
		riskFinal = riskFinal * 0.9;
	} else if (jrDevValue >= 25 && jrDevValue < 45) {
		riskFinal = riskFinal * 0.85;
	} else {
		riskFinal = riskFinal * 0.75;
	}
        //Testers, regardless of juinor or senior have tools available for testing. They are not programming an item from scratch.
	if (jrTestValue <= 15) {
		riskFinal = riskFinal * 0.9;
	} else if (jrTestValue > 15 && jrTestValue < 40) {
		riskFinal = riskFinal * 0.875;
	} else {
		riskFinal = riskFinal * 0.75;
	}
        //As more senior developers becomes involved with the project time, the returns rise in numbers. Senior developers are used to complex systems, so the understanding and skill set is available to be aware and provide positive influence on a project the more time they input. Complexity becomes more negligable the more senior a developer becomes.
	if (srDevValue < 10) {
		riskFinal = riskFinal * 0.925;
	} else if (srDevValue >= 10 && srDevValue < 35) {
		riskFinal = riskFinal * 0.975;
	} else if (srDevValue >= 35 && srDevValue < 65) {
		riskFinal = riskFinal * 1.015;
	} else {
		riskFinal = riskFinal * 1.05;
	}
        //Testers, regardless of juinor or senior have tools available for testing. They are not programming an item from scratch.
	if (srTestValue < 15) {
		riskFinal = riskFinal * 0.85;
	} else if (srTestValue >= 15 && srTestValue < 50) {
		riskFinal = riskFinal * 1.15;
	} else if (srTestValue >= 50 && srTestValue < 75) {
		riskFinal = riskFinal * 1.25;
	} else {
		riskFinal = riskFinal * 1.3;
	}
        //If everything is equal to the baseline values, then reset the schedule final variable as the previous if statements do not need to be added into the ultimate value.
	if (techWriterValue == 5 && prodManValue == 10 && jrDevValue == 27.5 && jrTestValue == 27.5 && srDevValue == 15 && srTestValue == 15) {
		//Reset this number as it's based off customer baseline data
		riskFinal = 140;
	}
	//For visual purposes, leaving anything over 180 at 165 so dial is clearly visible.
	if (riskFinal > 165) {
		riskFinal = 165;
	}

        //Rounding the risk up to two decimal places.
	riskFinalRound = riskFinal.toFixed(2);
	//Debugging purposes
	//console.log("This is the total risk of the project: " + riskFinalRound);


	//Set Schedule value final
	//------------------------
	//Based off customer data, the following percentage information is based off a median number set of tw=0.05, pm=0.1, jd=0.275, jt=0.275, sd=0.15, st=0.15.
	//  - The reason the if statements are seperated is due to simplisitc nature of schedule. For this design there is not a need to over complicate the algorithm becaues time is linear and can be adjusted as such. If there were to be a more complex version, then this section of code will expand greatly.
	//  - These if statements do not have a condition where the evaluation is equal to the integer being compared with. Reason: if they are all equal, then we are baselined and the schedule is equivalent to the weeks of contract.
        //The schedule final value is baselined at 125 because upon standards produced by the industry as well as the customer. This value will be adjusted later in the script during the genChartData() function call.
	//  - This is to level set the schedule based on complexity of the story and will be further manipulated below.
	//------------------------
	
	//Having more documentation for the developers and testers to reference will assist in decreasing schedule.
	if (techWriterValue < 5) {
		schedFinal = schedFinal - techWriterValue;
	} else if (techWriterValue >= 5) {
		schedFinal = schedFinal + techWriterValue;
	} else {
		schedFinal = schedFinal;
	}

        //Having additional time from the product manager will help understanding of the big picture and therefore decrease schedule.
	if (prodManValue < 10) {
		schedFinal = schedFinal - prodManValue;
	} else if (prodManValue >= 10) {
		schedFinal = schedFinal + prodManValue;
	} else {
		schedFinal = schedFinal;
	}

        //Notice the reverse math signs here, junior will cause greater delay instead of decreasing the schedule, but will have lower cost.
	if (jrDevValue > 27.5) {
		schedFinal = schedFinal - (jrDevValue / 2);
	} else if (jrDevValue <= 27.5 && jrDevValue >= 15) {
		schedFinal = schedFinal + (jrDevValue / 2);
	} else if (jrDevValue < 15) {
		schedFinal = schedFinal + jrDevValue;
	} else {
		schedFinal = schedFinal;
	}

        //Notice the reverse math signs here, junior will cause greater delay instead of decreasing the schedule, but will lower cost.
	if (jrTestValue > 27.5) {
		schedFinal = schedFinal - (jrTestValue / 2);
	} else if (jrTestValue <= 27.5 && jrTestValue >= 15) {
		schedFinal = schedFinal + (jrTestValue / 2);
	} else if (jrTestValue < 15) {
		schedFinal = schedFinal + jrTestValue;
	} else {
		schedFinal = schedFinal;
	}

        //Senior will help decrease schedule, but adversly increase cost.
	if (srDevValue < 15) {
		schedFinal = schedFinal - srDevValue;
	} else if (srDevValue >= 15 && srDevValue <= 22.5) {
		schedFinal = schedFinal + (srDevValue / 1.5);
	} else if (srDevValue > 22.5 && srDevValue <= 30) {
		schedFinal = schedFinal + (srDevValue/ 2);
	} else {
		schedFinal = schedFinal;
	}

        //Senior will help decrease schedule, but adversly increase cost.
	if (srTestValue < 15) {
		schedFinal = schedFinal - srTestValue;
	} else if (srTestValue >= 15 && srTestValue <= 22.5) {
		schedFinal = schedFinal + (srTestValue / 1.5);
	} else if (srTestValue > 22.5 && srTestValue <= 30) {
		schedFinal = schedFinal + (srTestValue / 2);
	} else {
		schedFinal = schedFinal;
	}

        //If everything is equal to the baseline values, then reset the schedule final variable as the previous if statements do not need to be added into the ultimate value.
	if (techWriterValue == 5 && prodManValue == 10 && jrDevValue == 27.5 && jrTestValue == 27.5 && srDevValue == 15 && srTestValue == 15) {
		//Reset this number as it's based off customer baseline data
		schedFinal = 125;
	}
	//For visual purposes, leaving anything over 180 at 165 so dial is clearly visible.
	if (schedFinal > 165) {
		schedFinal = 165;
	}

	//Debugging purposes
	//console.log("This is the final schedule of the project: " + schedFinal); 
        //#######################################################
	
	
	//This final code sets the values for the plotly charts, cost, risk, and schedule
	//costFinalChart is set under the cost section. It does not need rounding, therefore it did not need redundant placement.
	console.log(costFinalChart);
        riskFinalChart = riskFinal.toFixed(0);
	console.log(riskFinalChart);
	schedFinalChart = schedFinal.toFixed(0);
	console.log(schedFinalChart);

	//Generate and show plotly charts
        createCostPlot(costFinalChart);
	createRiskPlot(riskFinalChart);
	createSchedPlot(schedFinalChart);
}

function createCostPlot(costLevelParam) {
	//Debugging purposes
	//console.log('got cost');
        // Error checking for cost, if properly defined by user and function
        if (costLevel == null) {
        	costLevel = 1; 
        }

        // ----------------------------------------------------------------------
        // Trig to calc meter point
        var degrees = 180 - costLevelParam,
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
          height: chartW,
          width: chartH,
          xaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]},
          yaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]}
        };
        // ----------------------------------------------------------------------

	// Cost Plot is not needed until after variable finalization, so this function creates the chart after input paramters are sufficed.
	Plotly.newPlot('costPlotChart', costData, costLayout, {showSendToCloud:true});
}

function createSchedPlot(schedLevelParam) {
	//Debugging purposes
	//console.log('got sched');
        // Error checking for schedule, if properly defined by user and function
        if (schedLevel == null) {
        	schedLevel = 1; 
        }
        // ----------------------------------------------------------------------
        // Trig to calc meter point
        var degrees = 180 - schedLevelParam,
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
          height: chartW,
          width: chartH,
          xaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]},
          yaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]}
        };
        // ----------------------------------------------------------------------

	// Schedule Plot is not needed until after variable finalization, so this function creates the chart after input paramters are sufficed.
	Plotly.newPlot('schedulePlotChart', schedData, schedLayout, {showSendToCloud:true});
}

function createRiskPlot(riskLevelParam) {
	//Debugging purposes
	//console.log('got risk');
        // Error checking for level of risk, if properly defined by user and function
        if (riskLevel == null){
        	riskLevel = 1; 
        }
        // ----------------------------------------------------------------------
        // Trig to calc meter point
        var degrees = 180 - riskLevelParam,
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
          height: chartW,
          width: chartH,
          xaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]},
          yaxis: {zeroline:false, showticklabels:false,
                     showgrid: false, range: [-1, 1]}
        };
        // ----------------------------------------------------------------------

	// Risk Plot is not needed until after variable finalization, so this function creates the chart after input paramters are sufficed.
	Plotly.newPlot('riskPlotChart', riskData, riskLayout, {showSendToCloud:true});
}
