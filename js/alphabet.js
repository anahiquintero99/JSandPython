function Alphabet(pangram) {
  let alphabet = String.fromCharCode(...Array(123).keys())
    .slice(97)
    .split(",");
  pangramLowerCase = pangram.toLowerCase;
  for (const letter of alphabet) {
    const result = alphabet.filter((letter) => letter === pangramLowerCase);
  }

  console.log(alphabet);
}

pangram = "Cwm fjord bank glyphs vext quiz";
Alphabet(pangram);
//
