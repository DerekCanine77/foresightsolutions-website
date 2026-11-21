(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function reveal() {
    if (reduce || !("IntersectionObserver" in window)) return;
    var nodes = document.querySelectorAll(
      "main .hero, main .card, main .industry-card, main .signal-card, main .service-row, main .quote-panel, main .flow, main .contact-card"
    );
    if (!nodes.length) return;
    document.documentElement.classList.add("js");
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    Array.prototype.forEach.call(nodes, function (node) {
      node.classList.add("reveal");
      observer.observe(node);
    });
  }

  function selectFlow(tabs, panels, index) {
    tabs.forEach(function (tab, i) {
      var on = i === index;
      tab.setAttribute("aria-selected", on ? "true" : "false");
      tab.tabIndex = on ? 0 : -1;
      panels[i].hidden = !on;
    });
  }

  function flow() {
    var root = document.querySelector("[data-flow]");
    if (!root) return;
    var tabs = Array.prototype.slice.call(root.querySelectorAll("[role='tab']"));
    var panels = Array.prototype.slice.call(root.querySelectorAll("[role='tabpanel']"));
    if (!tabs.length || tabs.length !== panels.length) return;
    selectFlow(tabs, panels, 0);
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () {
        selectFlow(tabs, panels, i);
      });
      tab.addEventListener("keydown", function (event) {
        var next = null;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") next = (i + 1) % tabs.length;
        if (event.key === "ArrowLeft" || event.key === "ArrowUp") next = (i - 1 + tabs.length) % tabs.length;
        if (event.key === "Home") next = 0;
        if (event.key === "End") next = tabs.length - 1;
        if (next === null) return;
        event.preventDefault();
        selectFlow(tabs, panels, next);
        tabs[next].focus();
      });
    });
  }

  function assessment() {
    var form = document.querySelector("[data-assessment]");
    var out = document.getElementById("assessment-readout");
    if (!form || !out) return;
    form.addEventListener("submit", function (event) { event.preventDefault(); });
    form.addEventListener("change", render);

    function render() {
      var sets = Array.prototype.slice.call(form.querySelectorAll("fieldset"));
      var lines = [];
      var constraints = 0;
      var answered = 0;
      sets.forEach(function (set) {
        var chosen = set.querySelector("input:checked");
        if (!chosen) return;
        answered += 1;
        var legend = set.querySelector("legend");
        var label = chosen.closest("label");
        var question = legend ? legend.textContent.replace(/\s+/g, " ").trim() : "Question";
        var answer = label ? label.textContent.replace(/\s+/g, " ").trim() : chosen.value;
        lines.push(question + " " + answer + ".");
        if (chosen.getAttribute("data-constraint") === "yes") constraints += 1;
      });
      if (!answered) {
        out.textContent = "Answer the questions to see a readout of your own responses. Nothing is stored or sent.";
        return;
      }
      var text = "From your " + answered + (answered === 1 ? " answer: " : " answers: ") + lines.join(" ");
      text += " You marked " + constraints + " of those answers as a constraint. This only restates what you selected. It is not a benchmark.";
      var remaining = sets.length - answered;
      if (remaining) text += " " + remaining + (remaining === 1 ? " question is" : " questions are") + " still open.";
      out.textContent = text;
    }
  }

  reveal();
  flow();
  assessment();
})();
