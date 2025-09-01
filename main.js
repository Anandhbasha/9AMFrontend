// // Hoisting
// // a=10
// // console.log(a);

// // var a = 10
// // console.log(a);
// // var a =50
// // a=60
// // var a
// // a=70
// // console.log(a);

// // {
// //     var c=60
// // }
// // console.log(c);

// // console.log(a);
// // console.log(b);

// let b=20
// b=50
// // console.log(c);
// // {
// //     let d = 70
// // }
// // console.log(d);

// // const c = 30
// // c=60
// // console.log(c);

// // operators
//     // arithmetic Operator
//         // +,-,/,,*,%,++,--
// // ternary operator
// let age =18

// console.log(age>18?"Eligible":"Not Eligible");

// // data types
//     // primitive
//         // Number
//         let a=10
//         // String
//         let name = "xyz"
//         // Boolean
//         // True or False
//         is_comming = true
//         // undifined
//         let newname ;
//         // Null
//         let x = null
//     // Non premitive
//         // array
//         arr = [10,true,undefined,"names"] //10 = 0 - index
//         arr1 = [10,20,30,40]

//         // object

//         let person = {
//             name:"xyz",
//             age:25,
//             DOB:"12/12/12",
//             place:"CBE",
//             parents:{
//                 dad:"abc",
//                 mom:"def",
//                 sibling:{
//                     brother:"njkkjkh",
//                     sister:"aknbnbnb"
//                 }
//             }
//         }
//         // console.log(typeof(a));
//         console.log(arr);
//         console.log(arr[0]);
//         console.log(arr[1]);
//         console.log(arr[2]);
//         console.log(arr[3]);

//         console.log(person);
//         console.log(person.name);
//         console.log(person.parents.sibling.brother);
        
        
        
        
// function

// function add(a,b){
//     console.log(a+b);    
// }

// add(60,81)
// add(70,60)
// // add()
// // add()
// // add()
// // add()
// // // add()
// // Es6

// // arrow function
// const arrow = (a,b)=>console.log(a+b);
// arrow(5,6)
// // IFFI
// const IFFI = (function(){
//     console.log("IFFI is working");    
// })
// IFFI()
// // anoumous
// const ana = function(){}
// ana()

// Statements
let age = 20
// if(age>13){
//     console.log("He is Teenager");    
// }
// // if else
// if(age>13){
//     console.log("He is Teenager");    
// }
// else{
//     console.log("He is Child");    
// }

// else if
// if(age>13 && age<20){
//     console.log("He is Teenager");    
// }
// else if(age<13){
//     console.log("He is child");    
// }
// else{
//     console.log("Adult");    
// }

// nested if
// Nationality = "India"
// State = "TN"
// if(age>22){
//     console.log("Eligible to vote");
//     if(Nationality=="India"){
//         console.log("He is from India");
//         if(State === "TN"){
//             console.log("he can vote in TN");            
//         }
//     }
// }

// switch

let today = "Monday"

switch(today){
    case "Monday":
        console.log("Today is Monday");
        break
    case "Tuesday":
        console.log("Today is Tuesday");
        break
    case "Wednesday":
        console.log("Today is Wednesday");
        break
    case "Thursday":
        console.log("Today is Thursday");
        break
    case "Friday":
        console.log("Today is Friday");
        break
    case "Saturday":
        console.log("Today is Saturday");
        break
    default:
        console.log("Today is Sunday");
        
}


// looping Statements
// while
// let num1 = 10

// while(num1>num2){
//     console.log("While is working");
//     num2++    
// }

// // do while
// do{
//     console.log("Do while is working");    
// }while(1>5)
// for
// for(let num2=0;num1>num2;num2++){
//     console.log("For is working");    
// }

let arr1 = [50,545,6546,32154465,5341541,755]
// console.log(arr1[0]);
// console.log(arr1[1]);
// console.log(arr1[2]);
// console.log(arr1[3]);
// console.log(arr1[4]);
// console.log(arr1[5]);

// arrlength = 6
// arr Index = 0,1,2,3,4,5

// let x = 0
// while (x<arr1.length) { //0<6 1<6 6<6
//     console.log(arr1[x]);  //   50 545
//     ++x //x =0+1 = 1 6
    
// }

// for(let x=0;x<arr1.length;x++){
//     console.log(arr1[x]); 
// }
// for of
// for(let x of arr1){
//     console.log(x);    
// }
// // for in 
// for(let x in arr1){
//     console.log(x);    
//     console.log(arr1[x]);    
// }
// foreach

let name = "anandh"
// a
// an
// ana
// anan
// anandh

// h
// hd
// 
// anand
// anan
// ana
// an
// a
arr1.forEach((x)=>console.log(x))