// loops
let a = 10
// let b=20


// if(a<b){
//     console.log("condition is working");    
// }



// let arr = ["gayathri","paneer","netheesh","priyanka","santhani","madhu"]

// // console.log(arr[0]);
// // console.log(arr[1]);
// // console.log(arr[2]);
// // console.log(arr[3]);
// // console.log(arr[4]);
// // console.log(arr[5]);

// for(let a=0;a<arr.length;a++){
//     console.log(arr[a]);    
//     // console.log(x);
// }

// let names = "anandh"
// let temp = ""
// for(let a = 0;a<names.length;a++){
//     temp=temp+names[a] //a //an //ana //anan //anand //anandh
//     console.log(temp);   
// }



// // odd or even
// let oddEven = [42,33,11,84,55,37,6,7]

// for(let i=0;i<oddEven.length;i++){
//     temp = oddEven[i]
//     if(temp%2!=0){
//         console.log(temp);        
//     }
    
// }


// DOM



const Users = [
    {
        Sno:1,
        Name:"xyz",
        Age:22,
        City:"CBE"
    },
    {
        Sno:2,
        Name:"abc",
        Age:22,
        City:"Salem"
    },
    {
        Sno:3,
        Name:"def",
        Age:25,
        City:"Erode"
    },
    {
        Sno:4,
        Name:"wes",
        Age:20,
        City:"Karur"
    },
    {
        Sno:5,
        Name:"gth",
        Age:22,
        City:"CBE"
    },
]
let tableHead = ["Sno","Name","Age","City"]
let table = document.createElement('table')
let thead = document.createElement('thead')
for(let x =0;x<tableHead.length;x++){
    let th = document.createElement('th')
    th.innerHTML=tableHead[x]
    thead.appendChild(th)
}

let tbody = document.createElement('tbody')
let tr = document.createElement('tr')
let td = document.createElement('td')
tr.appendChild(td)
tbody.appendChild(tr)

table.appendChild(thead)
table.appendChild(tbody)
document.body.append(table)