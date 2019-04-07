import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import axios from 'axios';
import TextField from 'material-ui/TextField';
import UploadScreen from './UploadScreen';
class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: ''
        }
    }
    handleClick(event) {
        var apiBaseUrl = "http://localhost:5000/";
        var self = this;
        var payload = {
            "email": this.state.email,
            "password": this.state.password
        }
        axios.post(apiBaseUrl + 'login', payload)
            .then(function (response) {
                console.log(response);
                if (response.status == 200) {
                    console.log("Login successfull");
                    var uploadScreen = [];
                    uploadScreen.push(<UploadScreen appContext={self.props.appContext} />)
                    self.props.appContext.setState({ loginPage: [], uploadScreen: uploadScreen })
                }
                else if (response.status == 204) {
                    console.log("Username password do not match");
                    alert("username password do not match")
                }
                else {
                    console.log("Username does not exists");
                    alert("Username does not exist");
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    render() {
        return (<div>
            <MuiThemeProvider>
                <div>
                    <AppBar title="EasyAccounts" />
                    <TextField hintText="Enter your Username"
                        floatingLabelText="Email"
                        onChange={(event, newValue) => this.setState({ email: newValue })} />
                    <br />
                    <TextField hintText="Enter password"
                        floatingLabelText="Password"
                        onChange={(event, newValue) => this.setState({ password: newValue })} />
                    <br />
                    <RaisedButton label="Submit"
                        primary={true}
                        style={style}
                        onClick={(event) => this.handleClick(event)} />
                </div>
            </MuiThemeProvider>
        </div>)
    }

}
const style = {
    margin: 15,
}
export default Login;