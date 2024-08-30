const os = require('os');

console.log('informacion del sistema operativo:')
console.log('-------------------')

console.log('Nombre del sistema opertaivo', os.platform())
console.log('Version del sistema opertaivo', os.release())
console.log('Arquitectura', os.arch())
console.log('CPUs', os.cpus())
console.log('Memoria libre', os.freemem() / 1024 / 1024)
console.log('Memoria total', os.totalmem() / 1024 / 1024)
console.log('uptime', os.uptime() / 60 / 60)