import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { withStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import InputBase from '@material-ui/core/InputBase';
import NativeSelect from '@material-ui/core/NativeSelect';

export default class TxnPopup extends React.Component {


  handleClose = () => {
    this.props.displayPopup=false
  };

  render() {
    return (
      <div>
    <MuiThemeProvider>
     <Dialog
          open={this.props.displayPopup}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">Add Transaction</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Please enter the details of your new transaction.
            </DialogContentText>
            <TextField
              autoFocus
              hintText="Category"
              floatingLabelText="Category"
              margin="dense"
              id="name"
              type="email"
              fullWidth/>
          <InputLabel htmlFor="age-customized-native-simple" className={this.props.bootstrapFormLabel}>
            Transaction Type
          </InputLabel><br/>
          <NativeSelect
            // value={this.state.age}
            onChange={this.handleChange}
            input={<BootstrapInput name="age" id="age-customized-native-simple" />}
          >
            <option value={0}>Income</option>
            <option value={1}>Expense</option>
          </NativeSelect>
            <TextField
              autoFocus
              hintText="Quantity"
              floatingLabelText="Quantity"
              margin="dense"
              id="name"
              type="email"
              fullWidth/>
            <TextField
              autoFocus
              hintText="Amount"
              floatingLabelText="Amount"
              margin="dense"
              id="name"
              type="email"/>
          </DialogContent>
          <DialogActions>
            <RaisedButton label="Cancel"
                        primary={true}
                        onClick={(event) => this.handleClose(event)}/>
             
            <RaisedButton label="Submit"
                        primary={true}
                        onClick={(event) => this.handleClose(event)}/>
         </DialogActions>
        </Dialog>
        </MuiThemeProvider>
      </div>
    );
  }
}
const BootstrapInput = withStyles(theme => ({
    root: {
      'label + &': {
        marginTop: theme.spacing.unit * 3,
      },
    },
    input: {
      borderRadius: 4,
      position: 'relative',
      backgroundColor: theme.palette.background.paper,
      border: '1px solid #ced4da',
      fontSize: 16,
      width: 'auto',
      padding: '10px 26px 10px 12px',
      transition: theme.transitions.create(['border-color', 'box-shadow']),
      // Use the system font instead of the default Roboto font.
      fontFamily: [
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        'sans-serif',
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
      ].join(','),
      '&:focus': {
        borderRadius: 4,
        borderColor: '#80bdff',
        boxShadow: '0 0 0 0.2rem rgba(0,123,255,.25)',
      },
    },
  }))(InputBase);
  
  const styles = theme => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    margin: {
      margin: theme.spacing.unit,
    },
    bootstrapFormLabel: {
      fontSize: 18,
    },
  });
  