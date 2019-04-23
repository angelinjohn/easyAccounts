import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import axios from 'axios';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TxnPopup from './TxnPopup';
import DeleteIcon from '@material-ui/icons/Delete';
import Create from '@material-ui/icons/Create';
var apiBaseUrl = "http://localhost:5000/";
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

class SimpleTable extends React.Component{

 constructor(props){
     super(props);
     
     this.state={
        transactions:[],
        category: '',
          txntype: '',
          qty:'',
          amt:''
            }
 }
 displayPopup = () => {
    this.setState({ displayPopup: true });
    };
    closePopup = () => {
      this.setState({ displayPopup: false });
      };
    onSubmit = (event,payload) => {
      //API to save the payload
      var self = this;
      debugger;
      axios.post(apiBaseUrl +this.props.userId + '/transaction', payload)
            .then(function (response) {
            
              if (response.status == 200) {
                self.setState({
                    transactions: response.data
                })
              }
            
            })
      console.log(payload);
        this.setState({ displayPopup: false });
      }
 

 componentWillMount(){
    console.log(this.props);
   
      var self=this;
    axios.get(apiBaseUrl+this.props.userId + '/transactions')
        .then(function (response) {
            console.log(response);
         
            if (response.status == 200) {
                self.setState({
                    transactions: response.data,
                    displayPopup:false
                })
            }
 })
}

  render(){
    return (
    <div>
        <MuiThemeProvider>
    <AppBar title="Transaction"/>
     <Paper className={this.props.root}>
             <Table className={this.props.table}>
          <TableHead>
            <TableRow>
              <TableCell>Transaction Id</TableCell>
              <TableCell align="right">Category</TableCell>
              <TableCell align="right">Quantity</TableCell>
              <TableCell align="right">Transaction Type</TableCell>
              <TableCell align="right">Amount</TableCell>
              <TableCell align="right">Date</TableCell>
              <TableCell align="right"></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.transactions.map(transaction => (
              <TableRow key={transaction.txn_id}>
                <TableCell component="th" scope="row">
                  {transaction.txn_id}
                </TableCell>
                <TableCell align="right">{transaction.category}</TableCell>
                <TableCell align="right">{transaction.qty}</TableCell>
                <TableCell align="right">{transaction.txntype == 0?"Income":"Expense"}</TableCell>
                <TableCell align="right">{transaction.amt}</TableCell>
                <TableCell align="right">{transaction.date}</TableCell>
                {/* <TableCell align="right"><DeleteIcon onClick={(event) => this.deleteTxn(event,transaction.txn_id, transaction.user_id)}/>
                <Create onClick={(event) => this.editTxn(event,transaction, transaction.user_id)}/></TableCell> */}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
      <RaisedButton label="+ Add Transaction"
                    primary={true}
                    style={style}
                    onClick={(event) => this.displayPopup(event)} />
                    <RaisedButton label="Calculate your tax"
                    primary={true}
                    style={style}
                    onClick={(event) => this.handleClick(event)} />
        </MuiThemeProvider>
        <TxnPopup displayPopup={this.state.displayPopup} closePopup={() => this.closePopup()} onSubmit={(event,payload) => this.onSubmit(event,payload)}></TxnPopup>
      </div>
    )
            }

  }
  const style = {
    margin: 15,
}
  
  SimpleTable.propTypes = {
    props: PropTypes.object.isRequired,
  };

export default withStyles(styles)(SimpleTable);