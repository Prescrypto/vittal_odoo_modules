// @format

openerp.models_export_vittal = function(instance, local) {
  instance.web.ListView.include({
    render_buttons: function() {
      var btn;
      // GET BUTTON REFERENCE
      this._super.apply(this, arguments);
      if (this.$buttons) {
        btnExport = this.$buttons.find('.export_button');
        btnExportAll = this.$buttons.find('.export_all_button');
      }

      // PERFORM THE ACTION
      btnExport.on('click', this.proxy('export_button'));
      btnExportAll.on('click', this.proxy('export_all_button'));
    },
    export_button: function(event) {
      var type = event.target.dataset.type;
      var filename = event.target.dataset.filename + '.csv';
      new instance.web.Model(this.model)
        .call('export', [extractIds(this.records.records)], {
          context: instance.session.user_context,
        })
        .done(createCsv.bind(this, filename, type));
    },
    export_all_button: function(event) {
      var type = event.target.dataset.type;
      var filename = event.target.dataset.filename + '.completo.csv';
      new instance.web.Model(this.model)
        .call('export_all', [extractIds(this.records.records)], {
          context: instance.session.user_context,
        })
        .done(createCsv.bind(this, filename, type));
    }
  });
};

function extractIds(records) {
  return _.map(records, record => record.attributes.id);
}

function createCsv(filename, type, source) {
  console.log(source);
  var encodedUri = encodeURI('data:text/csv;charset=utf-8,' + source);
  var link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', filename);
  document.body.appendChild(link);
  link.click();
}