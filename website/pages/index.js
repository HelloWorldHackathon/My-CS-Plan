import Head from "next/head";

const request = require('request');

export default function Home() {
  return (
    <div class="container">
      <Head>
        <title>My CS Plans</title>
        <meta
          name="description"
          content="An optimization web application for Purdue CS concentrations"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1 class="title">Welcome to My CS Plans</h1>

      <h1>Concentrations:</h1>
      <h4>
        Please select 2{" "}
        <a href="#" id="why">
          why?
        </a>
      </h4>

      <div id="myModal" class="modal">
        <div class="modal-content">
          <span class="close">&times;</span>
          <p>
            Optimizing the least possible amount of classes between two
            concentrations is already super difficult! Trying to do so for
            three, four, etc. concentrations was beyond our ability for this
            Hackathon.
          </p>
          <p>
            It may seem like a straightforward problem, but when you consider
            that each concentration has required courses, requirements that you
            can select 1 of 2 or 3 options to fufill, an elective pool you can
            pull a certain number of courses out of to fufill a requirement, or
            a requirement that can be fufilled by taking any upper level class,
            it gets very difficult to optimize! Our algorithim is already
            unreasonably complicated in trying to address all these scenarios.
          </p>
          <p>2+ concentration optimization may be coming at a later date...</p>
        </div>
      </div>

      <form>
        <div class="threebythree">
          <div class="item">
            <label class="checkboxList">
              (Algorithmic) Foundations
              <input
                id="(Algorithmic) Foundations"
                type="checkbox"
                value="(Algorithmic) Foundations"
                name="check"
                onClick={() => onlyTwo("(Algorithmic) Foundations")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Computational Science and Engineering
              <input
                id="Computational Science and Engineering"
                type="checkbox"
                value="Computational Science and Engineering"
                name="check"
                onClick={() => onlyTwo("Computational Science and Engineering")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Computer Graphics and Visualization
              <input
                id="Computer Graphics and Visualization"
                type="checkbox"
                value="Computer Graphics and Visualization"
                name="check"
                onClick={() => onlyTwo("Computer Graphics and Visualization")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Database and Information Systems
              <input
                id="Database and Information Systems"
                type="checkbox"
                value="Database and Information Systems"
                name="check"
                onClick={() => onlyTwo("Database and Information Systems")}
              />
              <span class="checkmark"></span>
            </label>
          </div>

          <div class="item">
            <label class="checkboxList">
              Machine Intelligence
              <input
                id="Machine Intelligence"
                type="checkbox"
                value="Machine Intelligence"
                name="check"
                onClick={() => onlyTwo("Machine Intelligence")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Programming Language
              <input
                id="Programming Language"
                type="checkbox"
                value="Programming Language"
                name="check"
                onClick={() => onlyTwo("Programming Language")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Security
              <input
                id="Security"
                type="checkbox"
                value="Security"
                name="check"
                onClick={() => onlyTwo("Security")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Software Engineering
              <input
                id="Software Engineering"
                type="checkbox"
                value="Software Engineering"
                name="check"
                onClick={() => onlyTwo("Software Engineering")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Systems Software
              <input
                id="Systems Software"
                type="checkbox"
                value="Systems Software"
                name="check"
                onClick={() => onlyTwo("Systems Software")}
              />
              <span class="checkmark"></span>
            </label>
          </div>
        </div>
        <button
          class="submit-button"
          type="button"
          onClick={() => getTrack()}
        >
          Submit
        </button>
      </form>

      <hr />

      <div id="dynamicText">
        <h2 id="titleArea">Select some tracks!</h2>
        <div id="tableArea"></div>
      </div>

      <footer class="footer">
        <p>
          <a href="https://github.com/HelloWorldHackathon/" class="inlineLink">
            Built
          </a>{" "}
          by James, Jonathan, Noam, and, Pranav as part of Purdue's 2021 Hello
          World Hackathon.
        </p>
      </footer>
    </div>
  );
}

if (typeof window !== "undefined") {
  loadModal();
}

//Sets up map to correspond track name to it's internal number 
const tracksMap = new Map();
tracksMap.set('(Algorithmic) Foundations Track', 0);
tracksMap.set('Computational Science and Engineering Track', 1);
tracksMap.set('Computer Graphics and Visualization Track', 2);
tracksMap.set('Database and Information Systems Track"', 3);
tracksMap.set('Machine Intelligence Track', 4);
tracksMap.set('Programming Language Track', 5);
tracksMap.set('Security Track', 6);
tracksMap.set('Software Engineering Track', 7);
tracksMap.set('Systems Software Track', 8);

function getTrack() {
  var checkBox = document.getElementById("myCheck");

  // Gets names of tracks student selected and create a string of them, before setting title to the names of selected tracks
  let trackList = "Tracks selected: ";
  var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
  for (var checkbox of checkboxes) {
    trackList = trackList + checkbox.value + ", ";
  }
  trackList = trackList.slice(0, -2); //remove last comma
  document.getElementById("titleArea").innerHTML = trackList;

  var checkboxes = document.getElementsByName("check");

  let trackNumberArray = [];
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked == true) {
      trackNumberArray.push(tracksMap.get((checkboxes[i].value) + " Track"))
    }
  }

  fetch(`http://127.0.0.1:8081/${trackNumberArray[0]}/${trackNumberArray[1]}/`,
    {
      method: "GET",
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => response.text())
    .then(data => console.log(data));

  // Generates table from JSON optimized classes list and inserts it below

  let table = " ";
  /* INSERT LOOP CODE FOR JSON HERE*/

  //Sample table for visual purposes
  table =
    table +
    "<table>  <tr>    <th>Company</th>    <th>Contact</th>    <th>Country</th>  </tr>  <tr>    <td>Alfreds Futterkiste</td>    <td>Maria Anders</td>    <td>Germany</td>  </tr>  <tr>    <td>Centro comercial Moctezuma</td>    <td>Francisco Chang</td>    <td>Mexico</td>  </tr>  <tr>    <td>Ernst Handel</td>    <td>Roland Mendel</td>    <td>Austria</td>  </tr>  <tr>    <td>Island Trading</td>    <td>Helen Bennett</td>    <td>UK</td>  </tr>  <tr>    <td>Laughing Bacchus Winecellars</td>    <td>Yoshi Tannamuri</td>    <td>Canada</td>  </tr>  <tr>    <td>Magazzini Alimentari Riuniti</td>    <td>Giovanni Rovelli</td>    <td>Italy</td>  </tr></table>";

  document.getElementById("tableArea").innerHTML = table;
}

function onlyTwo(id) {
  var checkboxes = document.getElementsByName("check");
  let total = 0;
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked == true) {
      total++;
    }
  }
  if (total > 2) {
    document.getElementById(id).checked = false;
  }
}

function loadModal() {
  // Get the modal
  var modal = document.getElementById("myModal");

  // Get the button that opens the modal
  var btn = document.getElementById("why");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  btn.onclick = function () {
    modal.style.display = "block";
  };

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
}

