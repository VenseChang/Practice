import { Component } from '@angular/core';
import { NavController, AlertController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  name: string = "Tom";
  msg:  any = "Welcome!\r\nLet's make your own app by ionic!";

  constructor(
    public navCtrl: NavController,
    public alertCtrl: AlertController
  ) { }

  showAlert() {
    let alert = this.alertCtrl.create({
      title: this.name,
      message: this.msg.replace("\r\n", "<br>"),
      buttons: ['OK']
    });
    alert.present();
  }

}
