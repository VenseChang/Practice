import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  num: number = 0.0;
  register: number = 0.0;
  reset: boolean = false;
  process:string = null;
  dots: boolean = false;
  dotsNumCount: number = 0.1;

  constructor(public navCtrl: NavController) { }

  addNum(num: number):void{
    if(this.reset){
      this.num = 0;
      this.setResetStatus(false);
    }

    if(this.dots){
      num *= this.dotsNumCount;
      this.dotsNumCount *= 0.1;
    }else{
      this.num *= 10;
    }
    this.num = (this.num <0)? this.num - num : this.num + num;
  }

  cleanNum():void{
    this.num = 0;
    this.cleanDots();
  }

  cleanDots():void{
    this.dots = false;
    this.dotsNumCount = 0.1;
  }

  cleanAll():void{
    this.num = 0;
    this.register = 0;
    this.dots = false;
    this.dotsNumCount = 0.1;
  }

  negative():void{
    this.num *= -1;
  }

  divisionHun():void{
    this.num /= 100;
    this.setResetStatus(true);
  }

  plus():void{
    this.process = "add";
    this.register = this.num;
    this.setResetStatus(true);
  }

  minus():void{
    this.process = "minus";
    this.register = this.num;
    this.setResetStatus(true);
  }

  times():void{
    this.process = "times";
    this.register = this.num;
    this.setResetStatus(true);
  }

  division():void{
    this.process = "division";
    this.register = this.num;
    this.setResetStatus(true);
  }

  equals():void{
    switch (this.process) {
      case "add":
        this.num += this.register;
        break;
      case "minus":
      this.num = this.register - this.num;
        break;
      case "times":
      this.num *= this.register;
        break;
      case "division":
      this.num = this.register / this.num;
        break;
      default:
        break;
    }
    this.setResetStatus(true);
  }

  addDot():void{
    this.dots = true;
  }

  setResetStatus(status:boolean):void{
    this.reset = status;
    this.cleanDots();
  }
}
