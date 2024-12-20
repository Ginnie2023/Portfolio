"use strict";

const ps = require("prompt-sync");
const prompt = ps();

//car?
function ownCar(x) {
    if (x === "Y"){
        return isCar();
    }
    return null; 
}

//car travle
function isCar() {
    let fuel = prompt("How is your car powered? (Electric-E, Diesel-D, Gasoline-G): ")
    isFuel(fuel);
    if (fuel!="E"){
        let miles = prompt("Miles driven this year: ")
        let mpg = prompt("Average Miles Per Galon: ")
        carCarbonFP(miles,mpg,fuel)
    }

    return null;
}
//car travel carbon footprint
function carCarbonFP(miles,mpg,fuel){
    let gallons = miles/mpg;
    if (fuel === "G"){
        let carbon = 5.5
    }
}
// car fuel source 
function isFuel(x) {
    if (x === "E"){
        return isPower();
    }
    else if (x === "D" || x === "G"){
        return null; 
    }
        
}
//electric power source
function isPower(){
    let power = prompt("Is your car charged with renewable energy? (Y/N)")
    return power;
}

//public transportation 
function isPublic(x){
    if (x === "Y"){
        prompt("Bus, Subway, Train: ")
    }
    return null;
}

//main question 
let car = prompt("Do you/your family own a car? (Y/N): ")
ownCar(car);
let pub = prompt("Do you use public transportation regularly? (Y/N): ")
isPublic(pub);
//console.log('You\'ve driven '+ miles +' miles');