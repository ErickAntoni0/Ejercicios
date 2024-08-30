const path = require('node:path')

//barra separadora de carpetas segun SO
console.log(path.sep)

//unir rutas con path.join
const filePath = path.join('.','/content', 'subfolder', 'test.tx')
console.log(filePath)

const base = path.basename('/tmp/erick-secret-files/password.txt')
console.log(base)

const filename = path.basename('/tmp/erick-secret-files/password.txt', '.txt')
console.log(filename)

const extension = path.extname('my.super.image.jpg')
console.log(extension)