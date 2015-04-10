function create_graph(ddata){
  console.log(ddata);
  var margin = {top: 30, right: 20, bottom: 40, left: 50},
      width = 500 - margin.left - margin.right,
      height = 300 - margin.top - margin.bottom;

  var x0 = d3.scale.ordinal()
      .rangeRoundBands([0, width], .1);

  // var x1 = d3.scale.ordinal();
  var x1 = d3.scale.ordinal()
    .rangeBands([0, width], 0);
  var y = d3.scale.linear()
      .range([height, 0]);

  var color = d3.scale.ordinal()
      .range(["#ff0a60", "#0000ff"]);

  var xAxis = d3.svg.axis()
      .scale(x0)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .tickFormat(function(d) {
      	var format = d3.format(",.2s");
      	return '£' + format(d);
  	});

  var svg = d3.select("div.payGraph").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var data = [];
  // trim un-want values
  for (var i=0;i < ddata.values.length; i++){
    var finance_price = {};
    for (var key in ddata.values[i]){
      if(key !== 'Total Cost for Comparison')
        finance_price[key] = ddata.values[i][key]
    }
    data.push(finance_price);
  }
  console.log(data);

  var financial_options = d3.keys(data[0]).filter(function(key) { return key !== "financial_option" });

  data.forEach(function(d) {
    d.prices = financial_options.map(function(name) { return {name: name, value: +d[name]}; });
  });

  x0.domain(data.map(function(d) { return d.financial_option; }));
//   x1.domain(data.map(function(d) { return d.financial_option; }));
  x1.domain(financial_options).rangeRoundBands([0, x0.rangeBand()]);
  var max_price = d3.max(data, function(d) { 
    return d3.max(d.prices, function(d) { 
      return d.value;
    });
  })
  y.domain([0,d3.max([max_price, ddata.budget])]);
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end");

  var financial_option = svg.selectAll(".state")
      .data(data)
      .enter().append("g")
      .attr("class", "g")
      .attr("transform", function(d) { return "translate(" + x0(d.financial_option) + ",0)"; });

  financial_option.selectAll("rect")
      .data(function(d) { return d.prices; })
      .enter().append("rect")
      .attr("width", x1.rangeBand())
      .attr("x", function(d) { return x1(d.name); })
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .style("fill", function(d) { return color(d.name); });

  var legend = svg.selectAll(".legend")
      .data(financial_options.slice().reverse())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(10, -" + (i+1) * 12 + ")"; });

  legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", color);

  legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".01em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });
 
  var line = d3.svg.line()
      .x(function(d, i){
        if(i==0)
         return 0;
        else{
          return width;
        }})
      .y(function(d, i) { return y(ddata.budget); });

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

  svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", height + margin.bottom - 5)
        .attr("text-anchor", "middle")  
        .style("text-decoration", "underline");
};