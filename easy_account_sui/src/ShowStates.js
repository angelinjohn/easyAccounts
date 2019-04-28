import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

class ShowStates extends React.Component {
  render() {
    return (
      <div>
        <Dialog
          open={this.props.open}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
          <DialogTitle id="alert-dialog-title">{"See your better options!!"}</DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-description">
              <div>* Arizona</div>
              <div>* Alabama</div>
              <div>* California</div>
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => this.props.closeStatesPopup()} color="primary">
              OK
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
}

export default ShowStates;