function RoundToNearest15(date = new Date()) {
    const minutes = 15;
    const ms = 1000 * 60 * minutes;

    const manTime = new Date(Math.ceil(date.getTime() / ms) * ms)
    // rounds up to nearest 15min will return an error when nearest 15min == 0
    if (manTime.getMinutes() - new Date().getMinutes() > 15) {
      // so we reverse it a bit and add 60 so that it works
      return manTime.getMinutes() - new Date().getMinutes() + 60
    } else {
      return manTime.getMinutes() - new Date().getMinutes() - 1;
    };
}
  
  // 👇️ Mon Jan 24 2022 09:15:00 (minutes are 7)
console.log(RoundToNearest15(new Date(2022, 0, 24, 9, 7, 0)));
  
  // 👇️ Mon Jan 24 2022 09:15:00 (minutes are 8)
console.log(RoundToNearest15(new Date(2022, 0, 24, 9, 8, 0)));

  // 👇️ Should round to nearest 15 min
console.log(RoundToNearest15(new Date()));

export default RoundToNearest15