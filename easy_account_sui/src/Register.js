
import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from './Login'
class Register extends Component {
  constructor(props){
    super(props);
    this.state={
      first_name:'',
      last_name:'',
      email:'',
      password:'',
      state:'',
      city:'',
      dependents:'',
      cuisine:'',
    }
  }
  handleClick(event){
    var apiBaseUrl = "http://localhost:5000";
    console.log("values",this.state.first_name,this.state.last_name,this.state.email,this.state.password);
    //To be done:check for empty values before hitting submit
    var self = this;
    var payload={
    "name": this.state.first_name+" "+this.state.last_name,
    "email":this.state.email,
    "password":this.state.password,
    "state": this.state.state,
    "city": this.state.city,
    "dependents": this.state.dependents,
    "cuisine": this.state.cuisine,
    }
    axios.defaults.headers.post['Content-Type'] ='application/x-www-form-urlencoded';
    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    axios.post(apiBaseUrl+'/register', payload)
   .then(function (response) {
     console.log(response);
     if(response.status == 200){
      //  console.log("registration successfull");
       var loginscreen=[];
       loginscreen.push(<Login parentContext={this}/>);
       var loginmessage = "Not Registered yet.Go to registration";
       self.props.parentContext.setState({loginscreen:loginscreen,
       loginmessage:loginmessage,
       buttonLabel:"Register",
       isLogin:true
        });
     }
   })
   .catch(function (error) {
     console.log(error);
   });
  }
  render() {
    return (
      <div>
        <MuiThemeProvider>
          <div>
          <AppBar
             title="Register"
           />
           <TextField
             hintText="Enter your First Name"
             floatingLabelText="First Name"
             onChange = {(event,newValue) => this.setState({first_name:newValue})}
             />
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <TextField
             hintText="Enter your Last Name"
             floatingLabelText="Last Name"
             onChange = {(event,newValue) => this.setState({last_name:newValue})}
             />
           <br/>
           <TextField
             hintText="Enter your Email"
             type="email"
             floatingLabelText="Email"
             onChange = {(event,newValue) => this.setState({email:newValue})}
             />
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <TextField
             type = "password"
             hintText="Enter your Password"
             floatingLabelText="Password"
             onChange = {(event,newValue) => this.setState({password:newValue})}
             />
           <br/>
           <TextField
             hintText="Enter your state"
             floatingLabelText="State"
             onChange = {(event,newValue) => this.setState({state:newValue})}
             />
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <TextField
             hintText="Enter your city"
             floatingLabelText="City"
             onChange = {(event,newValue) => this.setState({city:newValue})}
             />
           <br/>
           <TextField
             hintText="Do you have any dependents"
             floatingLabelText="Dependents"
             onChange = {(event,newValue) => this.setState({dependents:newValue})}
             />
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <TextField
             hintText="Enter your preferred cuisine"
             floatingLabelText="Cuisine"
             onChange = {(event,newValue) => this.setState({cuisine:newValue})}
             />
           <br/>
           <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
          </div>
         </MuiThemeProvider>
      </div>
    );
  }
}
const style = {
  margin: 15,
};
export default Register;