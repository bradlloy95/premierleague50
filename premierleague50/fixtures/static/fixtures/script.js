const yesterday_btn = document.getElementById('yesterday_btn');
const tommorow_btn = document.getElementById('tomorrow_btn');


//const fixtures_content = Document.getElementById('fixtures_content');


yesterday_btn.addEventListener('click', function() {
    const fixtures_hearder = document.getElementById('fixtures_ctr_header')    
    const fixtures_content = document.getElementById('fixtures_content');
    const date = document.getElementById('fixutres_date')
    
    
    fetch("getFixtures?day=yesterday")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        
        //clear div
        fixtures_content.innerHTML = '';
        
            

            let formattedDateString = formatDate(data.dateViewed);
            date.innerText = formattedDateString
                if (data.count === 0){
                    let fixture = document.createElement('div');
                    fixture.classList.add('fixture');
                    fixture.innerHTML = `
                    <h1>No matches today</h1>`
                    fixtures_content.appendChild(fixture)
                }else {
                    data.serialized.forEach(fixture => {
                        console.log(fixture)
                        let game = document.createElement('div');
                        game.classList.add('fixture');
                        game.innerHTML = `
                        <div class="fixture_team">${fixture.serialized.hometeam}</div>
                        <div class="fixture_score">${fixture.serialized.homeScore}</div>
                        <div>VS</div>
                        <div class="fixture_score">${fixture.serialized.awayScore}</div>
                        <div class="fixture_team">${fixture.serialized.awayteam}</div>`

                        fixtures_content.appendChild(game)
                    })

                }
            

         
    })
   
})

tommorow_btn.addEventListener('click', function() {
    const fixtures_hearder = document.getElementById('fixtures_ctr_header')    
    const fixtures_content = document.getElementById('fixtures_content');
    const date = document.getElementById('fixutres_date')
    
    
    fetch("getFixtures?day=tomorrow")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        
        //clear div
        fixtures_content.innerHTML = '';
        
            

            let formattedDateString = formatDate(data.dateViewed);
            date.innerText = formattedDateString
                if (data.count === 0){
                    let fixture = document.createElement('div');
                    fixture.classList.add('fixture');
                    fixture.innerHTML = `
                    <h1>No matches today</h1>`
                    fixtures_content.appendChild(fixture)
                }else {
                    data.serialized.forEach(fixture => {
                        console.log(fixture)
                        let game = document.createElement('div');
                        game.classList.add('fixture');
                        game.innerHTML = `
                        <div class="fixture_team">${fixture.serialized.hometeam}</div>
                        <div class="fixture_score">${fixture.serialized.homeScore}</div>
                        <div>VS</div>
                        <div class="fixture_score">${fixture.serialized.awayScore}</div>
                        <div class="fixture_team">${fixture.serialized.awayteam}</div>`

                        fixtures_content.appendChild(game)
                        
                    })

                }
            

         
    })
   
})


// Function to format date from 'yyyy-mm-dd' to 'Month Day, Year'
function formatDate(inputDateStr) {
    // Parse the input date string
    var inputDate = new Date(inputDateStr);
    
    // Array of month names
    var monthNames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"];
    
    // Extract year, month, and day from the input date
    var year = inputDate.getFullYear();
    var monthIndex = inputDate.getMonth();
    var day = inputDate.getDate();
    
    // Construct the formatted date string
    var formattedDate = monthNames[monthIndex] + ' ' + day + ', ' + year;
    
    return formattedDate;
}


