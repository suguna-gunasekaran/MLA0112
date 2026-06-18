move(state(atdoor,onfloor,atwindow,hasnot),
     walk(window),
     state(atwindow,onfloor,atwindow,hasnot)).

move(state(atwindow,onfloor,atwindow,hasnot),
     climb,
     state(atwindow,onbox,atwindow,hasnot)).

move(state(atwindow,onbox,atwindow,hasnot),
     grasp,
     state(atwindow,onbox,atwindow,has)).