let test = "hej Hej på dig [#name], hur mår du, [#anus]?"

regex = /hej/gi
regex2 = /\[#(.*?)\]/i
regex3 = /\[#(.*?)\]/gi

function reg(reg) {
    if (reg[0] === '[#name]') return 'Johan'
    else return 'pucko'
}

let done = false
while (!done) {
    const res = test.replace(regex2, reg(test.match(regex2)))
    test = res
    if (test.match(regex3) === null) done = true
}


console.log(test)