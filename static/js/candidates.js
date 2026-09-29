/* Candidates page (Phase 3) — client-side search, filters and CSV export.
   Page-specific script: loaded only on /candidates, never from main.js. */

document.addEventListener("DOMContentLoaded", function () {
  var table = document.getElementById("candidates-table");
  if (!table) {
    return;
  }

  var rows = [].slice.call(table.querySelectorAll("tbody tr")).map(function (tr) {
    return { el: tr, data: JSON.parse(tr.getAttribute("data-row")) };
  });

  var searchInput = document.getElementById("candidate-search");
  var filterEls = [].slice.call(
    document.querySelectorAll(".candidates-toolbar [data-filter]")
  );
  var countEl = document.getElementById("candidate-count");
  var emptyEl = document.getElementById("candidates-empty");
  var tableWrap = table.closest(".table-container");
  var exportBtn = document.getElementById("export-csv");

  function rowMatches(row) {
    var q = searchInput.value.trim().toLowerCase();
    if (q) {
      var haystack = (
        row.name + " " + row.cid + " " + row.phone + " " + row.email
      ).toLowerCase();
      if (haystack.indexOf(q) === -1) {
        return false;
      }
    }
    for (var i = 0; i < filterEls.length; i++) {
      var el = filterEls[i];
      var key = el.getAttribute("data-filter");
      var val = el.value;
      if (!val) {
        continue;
      }
      if (key === "processed") {
        if ((val === "yes") !== row.processed) {
          return false;
        }
      } else if (String(row[key]) !== val) {
        return false;
      }
    }
    return true;
  }

  function apply() {
    var visible = 0;
    rows.forEach(function (row) {
      var show = rowMatches(row.data);
      row.el.style.display = show ? "" : "none";
      if (show) {
        visible++;
      }
    });
    if (countEl) {
      countEl.textContent =
        "Showing " + visible + " of " + rows.length + " candidates";
    }
    if (tableWrap) {
      tableWrap.style.display = visible ? "" : "none";
    }
    if (emptyEl) {
      emptyEl.hidden = visible !== 0;
    }
  }

  function clearFilters() {
    searchInput.value = "";
    filterEls.forEach(function (el) {
      el.value = "";
    });
    apply();
  }

  function csvEscape(value) {
    var s = String(value == null ? "" : value);
    return '"' + s.replace(/"/g, '""') + '"';
  }

  function exportCsv() {
    var header = [
      "Candidate", "Candidate ID", "Role", "JD Code", "Status",
      "Interview Date", "Slot", "Experience", "Track", "Tool Test",
    ];
    var lines = [header.map(csvEscape).join(",")];

    rows.forEach(function (row) {
      if (!rowMatches(row.data)) {
        return;
      }
      var d = row.data;
      lines.push(
        [
          d.name, d.cid, d.role, d.jd_code, d.status_label,
          d.date_label, d.slot, d.experience + " yrs", d.track, d.tool_test,
        ].map(csvEscape).join(",")
      );
    });

    var blob = new Blob(["\uFEFF" + lines.join("\r\n")], {
      type: "text/csv;charset=utf-8",
    });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "candidates-" + new Date().toISOString().slice(0, 10) + ".csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
  }

  searchInput.addEventListener("input", apply);
  filterEls.forEach(function (el) {
    el.addEventListener("change", apply);
  });
  [].slice.call(document.querySelectorAll(".js-clear-filters")).forEach(
    function (btn) {
      btn.addEventListener("click", clearFilters);
    }
  );
  if (exportBtn) {
    exportBtn.addEventListener("click", exportCsv);
  }
});
