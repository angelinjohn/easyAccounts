
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import axios from 'axios';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import ShowStates from './ShowStates';

const styles = theme => ({
    root: {
      width: '100%',
      marginTop: theme.spacing.unit * 3,
      overflowX: 'auto',
    },
    table: {
      minWidth: 700,
    },
  });
class Tax extends Component {
    showRanking = () => {
        this.setState({ displayRanking: true });
        var apiBaseUrl = "http://localhost:5000/";
        axios.get(apiBaseUrl+this.props.userId + '/predict')
         .then(function (response) {
            this.setState ({
                states: response.states
            });
        })
        };
        closeStatesPopup =() => {
            this.setState({ displayRanking: false });
        }

        componentWillMount() {
            var self = this;
            self.setState({
                displayRanking:false,
            })

        }
    render() {
        return (
            <div>
              <MuiThemeProvider>
          <AppBar title="Tax"/><div style={{padding:'100px'}}appContext={this.props.appContext} userId={this.props.userId}>Hey! We have calculated your tax to be ${this.props.tax}</div>
          <RaisedButton label="Do you want to explore better options ?"
                    primary={true}
                    style={style}
                    onClick={(event) => this.showRanking(event)} />
                    </MuiThemeProvider>
                    {this.state.displayRanking && (
                        <ShowStates open={true}  states={this.state.states} closeStatesPopup={() => this.closeStatesPopup()}/>
                    )}
                    </div>
        )
    }
}

const style = {
    margin: 15,
}

Tax.propTypes = {
    props: PropTypes.object.isRequired,
  };

export default withStyles(styles)(Tax);