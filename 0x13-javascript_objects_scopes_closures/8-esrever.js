#!/usr/bin/node
exports.esrever = function (list) {
  const reversArray = []
  list.map((val) => {
    reversArray.unshift(val)
  });
  return reversArray
}
