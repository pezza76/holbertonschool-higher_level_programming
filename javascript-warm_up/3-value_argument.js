#!/usr/bin/node

const args = process.argv

if (args.length - 2 === 0) {
    console.log("No argument")
} else {
    console.log(args[2])
}
