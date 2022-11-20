import csv
from string import Template

test_results = []
with open("TestAnalysisData.csv") as csv_file:
    file = csv.reader(csv_file)
    for row in file:
        test_results.append(row)

print(test_results)
# [['Test Name', 'NumberOfAsserts', 'NumberOfFailedAsserts'], ['Test 1', '32', '2'], ['Test 2', '31', '5'], ['Test 3', '27', '4'], ['Test 4', '14', '5'], ['Test 5', '14', '4'], ['Test 6', '22', '1'], ['Test 7', '47', '3'], ['Test 8', '26', '0'], ['Test 9', '12', '5'], ['Test 10', '8', '5'], ['Test 11', '34', '2'], ['Test 12', '40', '2'], ['Test 13', '24', '2'], ['Test 14', '2', '0'], ['Test 15', '46', '3'], ['Test 16', '8', '3'], ['Test 17', '44', '1'], ['Test 18', '49', '0'], ['Test 19', '26', '3'], ['Test 20', '25', '5'], ['Test 21', '13', '1'], ['Test 22', '9', '4'], ['Test 23', '41', '1'], ['Test 24', '30', '0'], ['Test 25', '33', '4'], ['Test 26', '23', '3'], ['Test 27', '13', '4'], ['Test 28', '40', '1'], ['Test 29', '33', '0'], ['Test 30', '18', '0'], ['Test 31', '27', '1'], ['Test 32', '33', '4'], ['Test 33', '1', '0'], ['Test 34', '18', '5'], ['Test 35', '12', '1'], ['Test 36', '31', '1'], ['Test 37', '50', '4'], ['Test 38', '4', '4'], ['Test 39', '31', '4'], ['Test 40', '8', '0']]

#convert data into integer type so that plot into graph
for data in test_results[1:]:
    data[1] = int(data[1])
    data[2] = int(data[2])

html_string = Template("""<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart(){
      var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.

    // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
      }
</script>
</head>
<body>
//Div that will hold the pie chart
    <div id="chart_div" style="width:1500; height:600"></div>
</body>
</html>""")

chart_data_str = ''
for row in test_results[1:]:
    chart_data_str += '%s, \n' % row
print(chart_data_str)

#substitute the data into the template
completed_html = html_string.substitute(labels=test_results[0], data=chart_data_str)

with open('column_chart2.html', 'w') as f:
    # write the html string you've create to a file
    f.write(completed_html)