function evenNumber(number = 0) {
  for (number = 0; number <= 50; number++) {
    if (number % 2 !== 0) {
      console.log(number + ": No es numero par");
    } else {
      console.log(number + ": Es numero par");
    }
  }
}

evenNumber();
