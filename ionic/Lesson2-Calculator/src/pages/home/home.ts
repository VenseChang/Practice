import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  num: any = 0;
  constructor(public navCtrl: NavController) {

  }

  addNum(num: number){
    this.num = this.num * 10 + num;
  }
}
