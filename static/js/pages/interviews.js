/* Interviews page — client-side search, filters, pagination and CSV export.
   Page-specific script: loaded only on /interviews. */

document.addEventListener("DOMContentLoaded", function () {
  var table = document.getElementById("interviews-table");
  if (!table) {
    return;
  }

  var rows = [].slice.call(table.querySelectorAll("tbody tr")).map(function (tr) {
    return { el: tr, data: JSON.parse(tr.getAttribute("data-row")) };
  });

  var searchInput = document.getElementById("interview-search");
  var filterEls = [].slice.call(document.querySelectorAll(".toolbar [data-filter]"));
  var emptyEl = document.getElementById("list-empty");
  var tableCard = document.getElementById("table-card");
  var exportBtn = document.getElementById("export-csv");

  var infoEl = document.getElementById("pagination-info");
  var pagesEl = document.getElementById("pagination-pages");
  var prevBtn = document.getElementById("pagination-prev");
  var nextBtn = document.getElementById("pagination-next");
  var sizeSel = document.getElementById("pagination-size");

  var state = { page: 1, pageSize: 10 };

  function rowMatches(row) {
    var q = searchInput.value.trim().toLowerCase();
    if (q) {
      var haystack = (
        row.candidate + " " + row.cid + " " + row.role + " " + row.interviewer
      ).toLowerCase();
      if (haystack.indexOf(q) === -1) {
        return false;
      }
    }
    for (var i = 0; i < filterEls.length; i++) {
      var el = filterEls[i];
      var key = el.getAttribute("data-filter");
      var val = el.value;
      if (val && String(row[key]) !== val) {
        return false;
      }
    }
    return true;
  }

  function visibleRows() {
    return rows.filter(function (r) {
      return rowMatches(r.data);
    });
  }

  function pageList(total, current) {
    var pages = [];
    var i;
    if (total <= 7) {
      for (i = 1; i <= total; i++) {
        pages.push(i);
      }
      return pages;
    }
    pages.push(1);
    var start = Math.max(2, current - 1);
    var end = Math.min(total - 1, current + 1);
    if (start > 2) {
      pages.push("\u2026");
    }
    for (i = start; i <= end; i++) {
      pages.push(i);
    }
    if (end < total - 1) {
      pages.push("\u2026");
    }
    pages.push(total);
    return pages;
  }

  function renderPagination(count) {
    var totalPages = Math.max(1, Math.ceil(count / state.pageSize));
    var from = count === 0 ? 0 : (state.page - 1) * state.pageSize + 1;
    var to = Math.min(state.page * state.pageSize, count);

    if (infoEl) {
      infoEl.textContent =
        "Showing " + from + "\u2013" + to + " of " + count + " interviews";
    }

    if (pagesEl) {
      pagesEl.innerHTML = "";
      pageList(totalPages, state.page).forEach(function (p) {
        if (p === "\u2026") {
          var ellipsis = document.createElement("span");
          ellipsis.className = "pagination__ellipsis";
          ellipsis.textContent = "\u2026";
          pagesEl.appendChild(ellipsis);
          return;
        }
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "page-btn" + (p === state.page ? " is-active" : "");
        btn.textContent = p;
        if (p === state.page) {
          btn.setAttribute("aria-current", "page");
        }
        btn.addEventListener("click", function () {
          state.page = p;
          apply();
        });
        pagesEl.appendChild(btn);
      });
    }

    if (prevBtn) {
      prevBtn.disabled = state.page <= 1;
    }
    if (nextBtn) {
      nextBtn.disabled = state.page >= totalPages;
    }
  }

  function apply() {
    var matched = visibleRows();
    var totalPages = Math.max(1, Math.ceil(matched.length / state.pageSize));
    if (state.page > totalPages) {
      state.page = totalPages;
    }
    var start = (state.page - 1) * state.pageSize;
    var end = start + state.pageSize;

    rows.forEach(function (row) {
      var idx = matched.indexOf(row);
      row.el.style.display =
        idx !== -1 && idx >= start && idx < end ? "" : "none";
    });

    renderPagination(matched.length);

    if (tableCard) {
      tableCard.style.display = matched.length ? "" : "none";
    }
    if (emptyEl) {
      emptyEl.hidden = matched.length !== 0;
    }
  }

  function clearFilters() {
    searchInput.value = "";
    filterEls.forEach(function (el) {
      el.value = "";
    });
    state.page = 1;
    apply();
  }

  function csvEscape(value) {
    var s = String(value == null ? "" : value);
    return '"' + s.replace(/"/g, '""') + '"';
  }

  function exportCsv() {
    var header = [
      "Candidate", "Candidate ID", "Role", "Interview Date", "Slot",
      "Interviewer", "Status", "Google Meet",
    ];
    var lines = [header.map(csvEscape).join(",")];

    visibleRows().forEach(function (row) {
      var d = row.data;
      lines.push(
        [
          d.candidate, d.cid, d.role, d.date_label, d.slot || "",
          d.interviewer, d.status, d.meet_url || "",
        ].map(csvEscape).join(",")
      );
    });

    var blob = new Blob(["\uFEFF" + lines.join("\r\n")], {
      type: "text/csv;charset=utf-8",
    });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "interviews-" + new Date().toISOString().slice(0, 10) + ".csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
  }

  searchInput.addEventListener("input", function () {
    state.page = 1;
    apply();
  });
  filterEls.forEach(function (el) {
    el.addEventListener("change", function () {
      state.page = 1;
      apply();
    });
  });
  [].slice.call(document.querySelectorAll(".js-clear-filters")).forEach(
    function (btn) {
      btn.addEventListener("click", clearFilters);
    }
  );
  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      if (state.page > 1) {
        state.page--;
        apply();
      }
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      state.page++;
      apply();
    });
  }
  if (sizeSel) {
    sizeSel.addEventListener("change", function () {
      state.pageSize = parseInt(this.value, 10) || 10;
      state.page = 1;
      apply();
    });
  }
  if (exportBtn) {
    exportBtn.addEventListener("click", exportCsv);
  }

  apply();
});
