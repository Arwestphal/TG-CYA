# hello

## Game Functions

graph TD
  a[Choose Your Adventure] --> b[user input]
  b -- 0 --> quit{quit}
  b -- 1 --> qd[Quick draw]
  b -- 2 --> zomb[Zombie survival]
  b -- 3 --> island[Island survival]
  b -- invalid --> b
  qd --> c[story = selection]
  zomb --> c
  island --> c
  c --> d[While game is running:]
  d --> e[set page text + options]
  e --> f[print page text + options]
  f --> g[user page input]
  g -- 0 --> a
  g -- valid --> h[page = choice]
  g -- invalid --> g
  h --> d