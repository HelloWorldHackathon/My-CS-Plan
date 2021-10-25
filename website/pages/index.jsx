import Head from "next/head";
import React from "react";

class Home extends React.Component {

    state = {
        CONST_TABLE_HEADER: (<tr>
            <th>Course Number</th>
            <th>Course Name</th>
            <th>Credit Hours</th>
        </tr>),
        tracks: [
            {
                name: "(Algorithmic) Foundations",
                id: 0
            }, {
                name: "Computational Science and Engineering",
                id: 1
            }, {
                name: "Computer Graphics and Visualization",
                id: 2
            }, {
                name: "Database and Information Systems",
                id: 3
            }, {
                name: "Machine Intelligence",
                id: 4
            }, {
                name: "Programming Language",
                id: 5
            }, {
                name: "Security",
                id: 6
            }, {
                name: "Software Engineering",
                id: 7
            }, {
                name: "Systems Software",
                id: 8
            }
        ],
        trackNumberArray: [],
        modalShown: false
    }

    componentDidMount() {
        // Prevent dissociation between this.state.trackNumberArray and the checked checkboxes
        // Browser might set it to checked by default; this sets it to be representative of the array
        this.forceUpdate();
    }

    render() {
        return (
            <div className="container"
                onClick={() => {
                    if (this.state.modalShown)
                        this.setState({modalShown: false});
                    }
                }
            >
                <Head>
                    <title>My CS Plans</title>
                    <meta name="description" content="An optimization web application for Purdue CS concentrations"/>
                    <link rel="icon" href="/favicon.ico"/>
                    <meta httpEquiv="Content-Security-Policy" content="upgrade-insecure-requests"/>
                </Head>
                <h1 className="title">Welcome to My CS Plans</h1>

                <h1>Concentrations:</h1>
                <h4>
                    Please select 2{" "}
                    <a href="#" onClick={() => {
                        this.setState({modalShown: true});
                    }}>
                        why?
                    </a>
                </h4>

                {this.state.modalShown ? (
                    <div className="modal">
                        <div className="modal-content">
                            <span className="close" onClick={() => {
                                    this.setState({modalShown: false})
                                }}>&times;</span>
                            <p>
                                Optimizing the least possible amount of classes between two concentrations is already super difficult! Trying to do so for three, four, etc. concentrations was beyond our ability for this Hackathon.
                            </p>
                            <p>
                                It may seem like a straightforward problem, but when you consider that each concentration has required courses, requirements that you can select 1 of 2 or 3 options to fufill, an elective pool you can pull a certain number of courses out of to fufill a requirement, or a requirement that can be fufilled by taking any upper level class, it gets very difficult to optimize! Our algorithim is already unreasonably complicated in trying to address all these scenarios.
                            </p>
                            <p>
                                2+ concentration optimization may be coming at a later date...
                            </p>
                        </div>
                    </div>
                ): <></>}
                <div className="threebythree">
                    {/* Important note here: It is iterating through all of the tracks. */}
                    {this.state.tracks.map((trackObj) => (
                        <div className="item" key={trackObj.id}>
                            <label className="checkboxList">
                                {trackObj.name}
                                <input
                                    type="checkbox"
                                    checked={this.state.trackNumberArray.includes(trackObj.id)}
                                    onChange={(event) => {
                                        // Set arr to trackNumberArray, for readability
                                        var arr = this.state.trackNumberArray;
                                        // If already in the array, you are unchecking the box
                                        if (arr.includes(trackObj.id)) {
                                            // Remove the selection from the array.
                                            arr.splice(arr.indexOf(trackObj.id), 1);
                                            this.forceUpdate();
                                            return;
                                        }
                                        // Otherwise, you checking the box.
                                        // So make sure you aren't going over the limit.
                                        if (arr.length == 2) {
                                            event.target.checked = false;
                                            return;
                                        }
                                        arr.push(trackObj.id);
                                        this.forceUpdate();

                                        // forceUpdate is used to refresh the page and show the box is checked.
                                    }}
                                />
                                <span className="checkmark"></span>
                            </label>
                        </div>
                    ))}
                </div>
                <button className="submit-button" type="button"
                    onClick={(e) => {
                        e.preventDefault();
                        this.getCourses(e);
                    }}
                >
                    Submit
                </button>
                <hr/>
                <div>
                    <h2>
                        {this.state.trackNumberArray.length == 0 ? (
                            "Select some tracks!"
                        ) : (
                            // Go through each selected id and map it to the corresponding name.
                            "Tracks Selected: " + this.state.trackNumberArray.map((id) => {
                                return this.state.tracks.filter((elem) => elem.id == id)[0].name;
                            }).join(", "))
                        }
                    </h2>
                    <div>
                        {/* Loading text to show its doing stuff while waiting. */}
                        {(!this.state.responseDataReceived && this.state.fetchingData) ? (
                            <h1>Loading...</h1>
                        ) : <></>}
                        {/* Only visible if the data is received from fetch. */}
                        {this.state.responseDataReceived ? (
                            this.state.fetchError ? (
                                <>
                                    <hr />
                                    <h3>An error occurred</h3>
                                    {/* errorMsg needs to be converted to a string, but no guarantees about if it has a toString method */}
                                    <h4> Error Msg:
                                        {this.state.errorMsg + ""}
                                    </h4>
                                </>
                            ) : (
                                <>
                                    <table>
                                        <tbody>
                                            {this.state.CONST_TABLE_HEADER}
                                            {this.state.responseData.courses.map((course) => (
                                                <tr key={course[0]}>
                                                    <td>{course[0]}</td>
                                                    <td>{course[1]}</td>
                                                    <td>{course[2]}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                    {[0, 1].map((electiveIndex) => {
                                        var electiveBank;
                                        switch (electiveIndex) {
                                            case 0:
                                                electiveBank = this.state.responseData.electives1;
                                                break;
                                            case 1:
                                                electiveBank = this.state.responseData.electives2;
                                                break;
                                        }
                                        if(electiveBank.required == 0)
                                            return (
                                                <h4>No electives available in Elective Bank {electiveIndex+1}.</h4>
                                            );
                                        return (
                                            <div key={electiveIndex}>
                                                <h4>
                                                    Elective Bank {electiveIndex + 1} (Required: {electiveBank.required})
                                                </h4>
                                                <table>
                                                    <tbody>
                                                        {this.state.CONST_TABLE_HEADER}
                                                        {
                                                            electiveBank.courses.map((course) => (<tr key={course[0]}>
                                                                <td>{course[0]}</td>
                                                                <td>{course[1]}</td>
                                                                <td>{course[2]}</td>
                                                            </tr>))
                                                        }
                                                    </tbody>
                                                </table>
                                            </div>
                                        );
                                    })}
                                </>
                            )
                        ): <></>}
                    </div>
                </div>

                <footer className="footer">
                    <p>
                        <a href="https://github.com/HelloWorldHackathon/" className="inlineLink">
                            Built
                        </a>{" "}
                        by James, Jonathan, Noam, and, Pranav as part of Purdue&apos;s 2021 Hello World Hackathon.
                    </p>
                </footer>
            </div>
        );
    }

    getCourses(event) {
        var trackNumberArray = this.state.trackNumberArray;

        this.setState({fetchingData: true, responseDataReceived: false});
        fetch(`/api/calculatecourses`, {
            method: "POST",
            body: JSON.stringify(trackNumberArray),
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => response.json()).then((jsonRes) => {
            if (!jsonRes.success) {
                console.log("Error: " + jsonRes.errorMsg);
                this.setState({responseDataReceived: true, fetchError: true, errorMsg: jsonRes.errorMsg});
                return;
            }
            let data = jsonRes.data;
            this.setState({responseDataReceived: true, fetchError: false, responseData: data});
        }).catch(err => {
            console.log(err);
            this.setState({responseDataReceived: true, fetchError: true, errorMsg: err.toString()});
        });
    }

}

export default Home;
