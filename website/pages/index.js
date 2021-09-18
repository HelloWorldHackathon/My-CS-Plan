import Head from "next/head";

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
      <form>
        <div class="threebythree">
          <div class="item">
            <label class="checkboxList">
              Computational Science and Engineering
              <input
                type="checkbox"
                value="Computational Science and Engineering"
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Computer Graphics and Visualization
              <input
                type="checkbox"
                value="Computer Graphics and Visualization"
              />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Database and Information Systems
              <input type="checkbox" value="Database and Information Systems" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              (Algorithmic) Foundations
              <input type="checkbox" value="(Algorithmic) Foundations" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Machine Intelligence
              <input type="checkbox" value="Machine Intelligence" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Programming Language
              <input type="checkbox" value="Programming Language" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Security
              <input type="checkbox" value="Security" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Software Engineering
              <input type="checkbox" value="Software Engineering" />
              <span class="checkmark"></span>
            </label>
          </div>
          <div class="item">
            <label class="checkboxList">
              Systems Software
              <input type="checkbox" value="Systems Software" />
              <span class="checkmark"></span>
            </label>
          </div>
        </div>
        <button class="submit-button" type="button" onClick={() => getTrack(" ")}>Submit</button>

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

function getTrack(track) {
  var checkBox = document.getElementById("myCheck");

  // Gets names of tracks student selected and create a string of them, before setting title to the names of selected tracks
  let trackList = "Tracks selected: ";
  var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
  for (var checkbox of checkboxes) {
    trackList = trackList + checkbox.value + ", ";
  }
  trackList = trackList.slice(0, -2); //remove last comma
  console.log(trackList);
  document.getElementById("titleArea").innerHTML = trackList;

  // Generates table from JSON optimized classes list and inserts it below 

  let table = " "
  /* INSERT LOOP CODE FOR JSON HERE*/

  //Sample table for visual purposes
  table = table + "<table>  <tr>    <th>Company</th>    <th>Contact</th>    <th>Country</th>  </tr>  <tr>    <td>Alfreds Futterkiste</td>    <td>Maria Anders</td>    <td>Germany</td>  </tr>  <tr>    <td>Centro comercial Moctezuma</td>    <td>Francisco Chang</td>    <td>Mexico</td>  </tr>  <tr>    <td>Ernst Handel</td>    <td>Roland Mendel</td>    <td>Austria</td>  </tr>  <tr>    <td>Island Trading</td>    <td>Helen Bennett</td>    <td>UK</td>  </tr>  <tr>    <td>Laughing Bacchus Winecellars</td>    <td>Yoshi Tannamuri</td>    <td>Canada</td>  </tr>  <tr>    <td>Magazzini Alimentari Riuniti</td>    <td>Giovanni Rovelli</td>    <td>Italy</td>  </tr></table>"

  document.getElementById("tableArea").innerHTML = table;
}
