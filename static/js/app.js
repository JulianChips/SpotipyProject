(async function (){
	const listGroup = d3.select("#results");
	const results = await d3.json("/api/features");
	const keys = ["Artist","Album","Song","Danceability","Energy","Key","Loudness","Mode","Speechiness","Acousticness","Instrumentalness","Liveness",
		"Valence","Tempo","URI","Duration_ms","Time_Signature"]
	if (results[0]!=null){
		for (let i = 0; i<keys.length; i++){
		const currentKey = keys[i]
		const listItem = listGroup.append("li")
			.classed("list-group-item d-flex justify-content-between align-items-center", true)
			.html(`${currentKey}`)
		const span = listItem.append("span")
			.classed("badge badge-primary badge-pill p-2",true)
			.html(`${results[0][currentKey.toLowerCase()]}`)
		}	
	}
	else{
		console.log("ERROR");
	}	
	
})()