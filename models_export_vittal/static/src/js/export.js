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
    },
  });
};

function extractIds(records) {
  return _.map(records, record => record.attributes.id);
}

function createCsv(filename, type, source) {
  var csv = csvBody(source, type);
  var encodedUri = encodeURI('data:text/csv;charset=utf-8,' + csv);
  var link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', filename);
  document.body.appendChild(link);
  link.click();
}

function csvBody(source, type) {
  var cleanSource = source.map(row => row.map(item => item.split('\n')[0]))
  var csvBody = cleanSource.join('\n');
  return [csvHeading(type), csvBody].join('\n');
}

function csvHeading(type) {
  // actualizar con /models/user_sales_order.py::export_client
  var clientHeader = [
    'Clave del Cliente',
    'Estatus',
    'Nombre',
    'R.F.C.',
    'Calle',
    'Número interior',
    'Número exterior',
    'Entre Calle',
    'Y Calle',
    'Colonia',
    'Código Postal',
    'Población',
    'Municipio',
    'Estado',
    'País',
    'Nacionalidad',
    'Referencia',
    'Teléfono',
    'Clasificación',
    'Fax',
    'Página web',
    'C.U.R.P.',
    'Clave de zona',
    'Imprimir',
    'Enviar por correo electrónico',
    'Envío silencioso',
    'Mail Predeterminado',
    'Día de revisión',
    'Día de pago',
    'Con crédito',
    'Días de crédito',
    'Limite de crédito',
    'Saldo',
    'Lista de precios',
    'Documento del último pago',
    'Monto del último pago',
    'Fecha del último pago',
    'Descuento',
    'Documento de última venta',
    'Monto de última venta',
    'Fecha de última venta',
    'Ventas anuales',
    'Clave de vendedor',
    'Tipo de empresa',
    'Matriz',
    'Calle de envío',
    'Núm. Int de envío',
    'Núm. Ext de envío',
    'Entre calle envío',
    'Y calle envío',
    'Colonia de envío',
    'Población de envío',
    'Municipio de envío',
    'Estado de envío',
    'País de envío',
    'Código postal de envío',
    'Clave de zona de envío',
    'Referencia de envío',
    'Cuenta contable',
    'Addenda de facturas',
    'Addenda de devolución',
    'Namespace del cliente',
    'Método de pago',
    'Número de cuenta',
    'Desglose de impuesto 1',
    'Desglose de impuesto 2',
    'Desglose de impuesto 3',
    'Desglose de impuesto 4',
    'Desglose personalizado',
    'Uso del CFDI',
    'Residencia fiscal',
    'Número de registro de identidad fiscal',
    'Forma de pago SAT',
    'Campo Libre 1',
    'Campo Libre 2',
    'Zona',
    'Campo Libre 4',
    'Campo Libre 5',
  ].join(',');

  var productHeader = [
    'Clave Artículo',
    'Descripción',
    'Línea',
    'Con serie',
    'Unidad de entrada',
    'Unidad de empaque',
    'Control de almacén',
    'Tiempo de surtido',
    'Stock mínimo',
    'Stock máximo',
    'Tipo de costeo',
    'Fecha de última compra',
    'Pendientes por recibir',
    'Fecha de última venta',
    'Pendientes por surtir',
    'Existencias',
    'Costo promedio',
    'Último costo',
    'Tipo de elemento',
    'Unidad de salida',
    'Factor entre unidades',
    'Apartados',
    'Con lote',
    'Con pedimento',
    'Peso',
    'volumen',
    'Clave de esquema',
    'Cantidad de ventas anuales',
    'Monto de ventas anuales',
    'Cantidad de compras anuales',
    'Monto de compras anuales',
    'Cuenta contable',
    'Estatus',
    'Manejo de IEPS',
    'Numero de impuesto a aplicar',
    'Cuota de IEPS',
    'Forma de aplicar IEPS',
    'Clave SAT',
    'Clave unidad',
    'Clave Erste',
    'Campo libre 2',
    'Campo libre 3',
    'Campo libre 4',
    'Campo libre 5',
    'Campo libre 6',
  ];

  var orderHeader = [
    'Clave',
    'Cliente',
    'Fecha de elaboración',
    'Descuento financiero',
    'Observaciones',
    'Clave de vendedor',
    'Su pedido',
    'Fecha de entrega',
    'Fecha de vencimiento',
    'Precio',
    'Desc. 1',
    'Desc. 2',
    'Desc. 3',
    'Comisión',
    'Clave de esquema de impuestos',
    'Clave del artículo',
    'Cantidad',
    'I.E.P.S.',
    'Impuesto 2',
    'Impuesto 3',
    'I.V.A.',
    'Observaciones de partida',
  ];

  var header;

  switch (type) {
    case 'clients':
      header = clientHeader;
      break;
    case 'products':
      header = productHeader;
      break;
    case 'orders':
      header = orderHeader;
      break;
  }

  return header;
}
