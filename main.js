// // // Hoisting
// // // a=10
// // // console.log(a);

// // // var a = 10
// // // console.log(a);
// // // var a =50
// // // a=60
// // // var a
// // // a=70
// // // console.log(a);

// // // {
// // //     var c=60
// // // }
// // // console.log(c);

// // // console.log(a);
// // // console.log(b);

// // let b=20
// // b=50
// // // console.log(c);
// // // {
// // //     let d = 70
// // // }
// // // console.log(d);

// // // const c = 30
// // // c=60
// // // console.log(c);

// // // operators
// //     // arithmetic Operator
// //         // +,-,/,,*,%,++,--
// // // ternary operator
// // let age =18

// // console.log(age>18?"Eligible":"Not Eligible");

// // // data types
// //     // primitive
// //         // Number
// //         let a=10
// //         // String
// //         let name = "xyz"
// //         // Boolean
// //         // True or False
// //         is_comming = true
// //         // undifined
// //         let newname ;
// //         // Null
// //         let x = null
// //     // Non premitive
// //         // array
// //         arr = [10,true,undefined,"names"] //10 = 0 - index
// //         arr1 = [10,20,30,40]

// //         // object

// //         let person = {
// //             name:"xyz",
// //             age:25,
// //             DOB:"12/12/12",
// //             place:"CBE",
// //             parents:{
// //                 dad:"abc",
// //                 mom:"def",
// //                 sibling:{
// //                     brother:"njkkjkh",
// //                     sister:"aknbnbnb"
// //                 }
// //             }
// //         }
// //         // console.log(typeof(a));
// //         console.log(arr);
// //         console.log(arr[0]);
// //         console.log(arr[1]);
// //         console.log(arr[2]);
// //         console.log(arr[3]);

// //         console.log(person);
// //         console.log(person.name);
// //         console.log(person.parents.sibling.brother);
        
        
        
        
// // function

// // function add(a,b){
// //     console.log(a+b);    
// // }

// // add(60,81)
// // add(70,60)
// // // add()
// // // add()
// // // add()
// // // add()
// // // // add()
// // // Es6

// // // arrow function
// // const arrow = (a,b)=>console.log(a+b);
// // arrow(5,6)
// // // IFFI
// // const IFFI = (function(){
// //     console.log("IFFI is working");    
// // })
// // IFFI()
// // // anoumous
// // const ana = function(){}
// // ana()

// // Statements
// let age = 20
// // if(age>13){
// //     console.log("He is Teenager");    
// // }
// // // if else
// // if(age>13){
// //     console.log("He is Teenager");    
// // }
// // else{
// //     console.log("He is Child");    
// // }

// // else if
// // if(age>13 && age<20){
// //     console.log("He is Teenager");    
// // }
// // else if(age<13){
// //     console.log("He is child");    
// // }
// // else{
// //     console.log("Adult");    
// // }

// // nested if
// // Nationality = "India"
// // State = "TN"
// // if(age>22){
// //     console.log("Eligible to vote");
// //     if(Nationality=="India"){
// //         console.log("He is from India");
// //         if(State === "TN"){
// //             console.log("he can vote in TN");            
// //         }
// //     }
// // }

// // switch

// let today = "Monday"

// switch(today){
//     case "Monday":
//         console.log("Today is Monday");
//         break
//     case "Tuesday":
//         console.log("Today is Tuesday");
//         break
//     case "Wednesday":
//         console.log("Today is Wednesday");
//         break
//     case "Thursday":
//         console.log("Today is Thursday");
//         break
//     case "Friday":
//         console.log("Today is Friday");
//         break
//     case "Saturday":
//         console.log("Today is Saturday");
//         break
//     default:
//         console.log("Today is Sunday");
        
// }


// // looping Statements
// // while
// // let num1 = 10

// // while(num1>num2){
// //     console.log("While is working");
// //     num2++    
// // }

// // // do while
// // do{
// //     console.log("Do while is working");    
// // }while(1>5)
// // for
// // for(let num2=0;num1>num2;num2++){
// //     console.log("For is working");    
// // }

// let arr1 = [50,545,6546,32154465,5341541,755]
// // console.log(arr1[0]);
// // console.log(arr1[1]);
// // console.log(arr1[2]);
// // console.log(arr1[3]);
// // console.log(arr1[4]);
// // console.log(arr1[5]);

// // arrlength = 6
// // arr Index = 0,1,2,3,4,5

// // let x = 0
// // while (x<arr1.length) { //0<6 1<6 6<6
// //     console.log(arr1[x]);  //   50 545
// //     ++x //x =0+1 = 1 6
    
// // }

// // for(let x=0;x<arr1.length;x++){
// //     console.log(arr1[x]); 
// // }
// // for of
// // for(let x of arr1){
// //     console.log(x);    
// // }
// // // for in 
// // for(let x in arr1){
// //     console.log(x);    
// //     console.log(arr1[x]);    
// // }
// // foreach

// let names = "anandh"
// // a
// // an
// // ana
// // anan
// // anandh
// let temp=""
// // for(let x of names){
// //     temp+=x
// //     console.log(temp);    
// // }

// for(let x=names.length-1;x>=0;x--){
//     temp+=names[x]
//     console.log(temp);   
// }

// // h
// // hd
// // 
// // anand
// // anan
// // ana
// // an
// // a
// arr1.forEach((x)=>console.log(x))


// // push
// let arra2 = [20,44,52,88]
// arra2.push(100)
// console.log(arra2);
// arra2[5] = 500
// console.log(arra2);


// // pop
// arra2.pop()
// console.log(arra2);

// // shift
//     arra2.shift()
//     console.log(arra2);
    
// // unshift
//     arra2.unshift(600)
//     console.log(arra2);
// // indexof
// console.log(arra2.indexOf(600));

// // includes
// console.log(arra2.includes(660));
// // map
//     arra2.map((item)=>console.log(item))
// // reduce
// let total = arra2.reduce((acc,sum)=>acc+sum)//sum=600 acc=0
// console.log(total);

// // filter
// console.log(arra2.filter((item)=>item%3==0));

// // sort
// let array1 = ['a',"c","d","b"]
// let array2 = [10,20,13,15,16]
// array1.sort()
// array2.sort()
// console.log(array1);
// console.log(array2);
// // reverse
// array1.reverse()
// array2.reverse()
// console.log(array1);
// console.log(array2);
// // concat
// let a = [1,2]
// let b = [2,3]
// console.log(a.concat(b));

// // find
// console.log(a.find((x)=>x==10));

// // slice
// console.log(array1.slice(0,2));

// // splice
// let fruits = ['apple','kiwi','orange']
// fruits.splice(1,1,'grapes')
// console.log(fruits);


// // join
// let words = ["Hello","World"]
// console.log(words.join(" "));

// // split
// let newName = "Arun kumar"
// let newValue = newName.split(" ")
// console.log(newValue)

// // setTimeout
// setTimeout(()=>{
//     console.log("Set timeout is working");    
// },5000)
// // setInterval
// setInterval(()=>{
//     console.log("Set interval is working");    
// },2000)


// async
    // promise
    // async awiat
    // fetch
    // trycatch

// let newPromise  = new Promise((resolved,reject)=>{
//     let bookTicket = false
//     if(bookTicket){
//         resolved("Ticket Boooked Sucessfully")
//     }
//     else{
//         reject("Unable to book the ticket")
//     }
// })

// newPromise.then((result)=>{
//     console.log(result) 
// }).catch((err)=>{console.log(err)})


// let friend1 = new Promise((resolved,reject)=>{
//     let reached = true
//     if(reached){
//         resolved("friend1 reached home")
//     }
//     else{
//         reject("Not yet reached")
//     }
// })
// let friend2 = new Promise((resolved,reject)=>{
//     let reached = true
//     if(reached){
//         resolved("friend2 reached home")
//     }
//     else{
//         reject("friend2 Not yet reached")
//     }
// })
// let friend3 = new Promise((resolved,reject)=>{
//     let reached = false
//      setTimeout(()=>{
//     if(reached){       
//             resolved("friend3 reached home")   }
  
//     else{
//         reject("friend3 Not yet reached")
//     }
//       },5000)
// })

// // Promise.race([friend1,friend2,friend3]).then((res)=>{
// //     console.log(res) 
// // }).catch((err)=>{console.log(err)})
// // Promise.any([friend1,friend2,friend3]).then((res)=>{
// //     console.log(res) 
// // }).catch((err)=>{console.log(err)})
// // Promise.all([friend1,friend2,friend3]).then((res)=>{
// //     console.log(res) 
// // }).catch((err)=>{console.log(err)})
// Promise.allSettled([friend1,friend2,friend3]).then((res)=>{
//     console.log(res) 
// }).catch((err)=>{console.log(err)})


// return


// function add(a,b){
//     return a+b    
// }

// console.log(add(150,220));

// let fetchData = new Promise((resolved,reject)=>{
//     fetch('https://jsonplaceholder.typicode.com/posts').then((res)=>{
//         if(!res.ok){
//             reject("Unable to connect API")
//         }
//         else{
//             resolved(res.json())            
//         }    })
// })

// fetchData.then((result)=>{console.log(result)})
// .catch((err)=>console.log(err))
// async
// let fetchData = async()=>{
//     try{
//         let res = await fetch('https://jsonplaceholder.typicode.com/po')
//     if(!res.ok){
//         throw Error ("Unable to connect")
//     }
//     const data =  await res.json()
//     console.log(data);
//     }
//     catch(err){
//         console.log(err);
        
//     }    
// }

// fetchData()


















const loadData = async()=>{
    try{
        const res = await fetch('https://jsonplaceholder.typicode.com/posts')
        if(!res.ok){
            throw Error("Unable to connect")
        }
        const datas = await res.json()
        console.log(datas);
    }
    catch(err){
        console.log(err);
        
    }
    
    
}
loadData()


// const comingToClass = new Promise((resolved,reject)=>{
//     let coming = false
//     if(!coming){
//         reject("Still not came")
//     }
//     else{
//         resolved("He is arrived")
//     }
// })
// comingToClass.then((res)=>{
//     console.log(res)    
// }).catch((err)=>{
//     console.log(err);    
// })

// DOM
// let btn = document.createElement('button')

// btn.innerHTML = "Click"

// document.body.append(btn)


// btn.addEventListener('click',()=>{
//     btn.style.backgroundColor="red"
//     btn.innerHTML ==="Click"?btn.innerText = "Clicked":btn.innerText ="Click"
// })

const datas = [
    {id:1,name:"xyz",city:"cbe"},
    {id:2,name:"abc",city:"salem"},
    {id:3,name:"def",city:"erode"},
    {id:4,name:"saw",city:"karur"},
    {id:5,name:"awe",city:"trichy"},
    {id:6,name:"ver",city:"chennai"},
    {id:7,name:"eff",city:"pondy"},
    {id:8,name:"wer",city:"ooty"},
    {id:9,name:"jhg",city:"pollachi"},
    {id:10,name:"ilk",city:"cbe"},
]


const div = document.createElement('div')
const table = document.createElement('table')
const thead = document.createElement('thead')
const tbody = document.createElement('tbody')
const th = document.createElement('th')
const tr = document.createElement('tr')
const td = document.createElement('td')

div.appendChild(table)
table.appendChild(thead)
thead.appendChild(th)
table.appendChild(tbody)
tbody.appendChild(tr)
tr.appendChild(td)
document.body.append(div)


// console.log(datas);
// 

// let button = document.getElementById('btn')
// let button = document.querySelector('#btn')
// let button = document.querySelectorAll('.btn')
// let button = document.getElementsByTagName('button')
let button = document.getElementsByClassName('button')
const btnClick = ()=>{
    button.textContent = "OFF"
}