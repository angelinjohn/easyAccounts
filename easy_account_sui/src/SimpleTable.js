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
        transactions:[]
            }

 }
    handleClick = () => {
    this.setState({ displayPopup: true });
    };
 

 componentWillMount(){
    console.log(this.props);
    var apiBaseUrl = "http://localhost:5000/";
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
                <TableCell align="right">{transaction.txntype}</TableCell>
                <TableCell align="right">{transaction.amt}</TableCell>
                <TableCell align="right">{transaction.date}</TableCell>
                <TableCell align="right"><DeleteIcon /><Create/></TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
      <RaisedButton label="+ Add Transaction"
                    primary={true}
                    style={style}
                    onClick={(event) => this.handleClick(event)} />
        </MuiThemeProvider>
        <TxnPopup displayPopup={this.state.displayPopup}></TxnPopup>
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