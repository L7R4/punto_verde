const labels_container = document.querySelector(".highcharts-axis-labels")

let text_happy = document.querySelector(".highcharts-axis-labels :nth-child(1)")
let text_neutral = document.querySelector(".highcharts-axis-labels :nth-child(2)")
let text_sad = document.querySelector(".highcharts-axis-labels :nth-child(3)")

const image_happy = document.createElement('img')
const image_neutral = document.createElement('img')
const image_sad = document.createElement('img')

image_happy.src = "../static/images/happy_face.png"

text_happy.replace(text_happy,image_happy)