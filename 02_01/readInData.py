import csv

# final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

timing_data = []
with open("TestTimingData.csv") as csv_file:
    # csv.filereader(fileName) can make every row into list
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

chart_data = [["Test Name", "Diff from Avg"]]
table_data = [["Test Name", "Run Time"]]

for data in timing_data[1:]:
    test_name = data[0]
    # skipt the none/ blank data in data[1] or data[2]
    if not data[1] or not data[2]:
        continue
    run_time = float(data[1])
    avg_run_time = float(data[2])
    diff_from_avg = avg_run_time - run_time
    chart_data.append([test_name, diff_from_avg])
    table_data.append([test_name, run_time])

print(f"chart_data = {chart_data}")
print(f"table_data = {table_data}")

# chart_data = [['Test Name', 'Diff from Avg'], ['Test 1', -133.0], ['Test 2', -64.0], ['Test 4', -135.0], ['Test 5', 168.0], ['Test 6', 35.0], ['Test 7', -39.0], ['Test 8', 50.0], ['Test 9', 143.0], ['Test 10', -79.0], ['Test 11', 133.0], ['Test 12', 56.0], ['Test 13', -134.0], ['Test 14', 49.0], ['Test 15', -39.0], ['Test 16', -38.0], ['Test 18', 50.0], ['Test 19', -130.0], ['Test 20', 131.0], ['Test 21', 102.0], ['Test 22', -64.0], ['Test 23', 75.0], ['Test 24', -173.0], ['Test 25', -53.0], ['Test 26', 96.0], ['Test 27', 15.0], ['Test 28', 13.0], ['Test 29', -18.0], ['Test 30', -76.0], ['Test 31', -15.0], ['Test 32', -19.0], ['Test 33', 205.0], ['Test 34', -28.0], ['Test 35', 15.0], ['Test 36', 26.0], ['Test 37', -41.0], ['Test 38', 113.0], ['Test 39', -110.0], ['Test 40', 15.0]]
# table_data = [['Test Name', 'Run Time'], ['Test 1', 193.0], ['Test 2', 79.0], ['Test 4', 192.0], ['Test 5', 49.0], ['Test 6', 119.0], ['Test 7', 150.0], ['Test 8', 70.0], ['Test 9', 81.0], ['Test 10', 161.0], ['Test 11', 72.0], ['Test 12', 120.0], ['Test 13', 138.0], ['Test 14', 25.0], ['Test 15', 113.0], ['Test 16', 246.0], ['Test 18', 165.0], ['Test 19', 246.0], ['Test 20', 49.0], ['Test 21', 93.0], ['Test 22', 168.0], ['Test 23', 95.0], ['Test 24', 198.0], ['Test 25', 113.0], ['Test 26', 153.0], ['Test 27', 41.0], ['Test 28', 116.0], ['Test 29', 182.0], ['Test 30', 222.0], ['Test 31', 243.0], ['Test 32', 53.0], ['Test 33', 10.0], ['Test 34', 161.0], ['Test 35', 138.0], ['Test 36', 107.0], ['Test 37', 83.0], ['Test 38', 21.0], ['Test 39', 234.0], ['Test 40', 132.0]]


# Using google chart API - load the chart lib
# https://developers.google.com/chart/interactive/docs/datatables_dataviews
# DRAW chart - https://developers.google.com/chart/interactive/docs/basic_draw_chart
from string import Template

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
    <div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s, \n' % row

completed_html = html_string.substitute(labels=chart_data[0], data=chart_data_str)

with open('column_chart.html', 'w') as f:
    f.write(completed_html)

