const form =document.getElementById('main-con')
const btn2 =document.getElementById('btn2')
const span = document.getElementById("span")
const btn = document.getElementById('btn1')
const wrong = document.getElementById('wrong')
const check = document.getElementById("check")
const password = document.getElementById("textInput5")
const Name = document.getElementById('name')
const nameinput = document.getElementById('textInput')

span.addEventListener("click", ()=>{
    form.style.display = 'none'
    btn2.style.display = 'block'
})
btn2.addEventListener("click", () =>{
    form.style.display  = 'flex'
})
btn.addEventListener("click", () =>{
    wrong.classList.toggle("wrongN")
})
check.addEventListener('click', ()=>{
if ( password.type === "password") {
    password.type = "text"
} else {
    password.type = "password"
}
})
Name.textContent = nameinput.value