import Head from "next/head";
import Image from "next/image";

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
      <div class="threebythree">
        <div class="item">
          <label class="checkboxList">
            Computational Science and Engineering
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Computer Graphics and Visualization
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Database and Information Systems Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>

        <div class="item">
          <label class="checkboxList">
            (Algorithmic) Foundations Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Machine Intelligence Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Programming Language Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>

        <div class="item">
          <label class="checkboxList">
            Security Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Software Engineering
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="item">
          <label class="checkboxList">
            Systems Software Track
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </div>
      </div>

      <hr />

      <p> hello i am dynamic content!</p>

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
