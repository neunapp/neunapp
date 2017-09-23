new Vue({
  el: 'app',
  delimiters: ['{$', '$}'],

  //funcion de cilco de vida
  mounted() {
    var self = this;
    axios.get('/api/cotizacion/questions/')
      .then(function (response) {
        self.questions = response.data;
        self.question = response.data[self.indice];
        self.cargar_respuesta(self.question['id']);
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    cargar_respuesta: function(pk) {
      var self = this;
      axios.get('/api/cotizacion/questions/answer/'+pk+'/')
        .then(function (response) {
          self.answers = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    nueva_pregunta: function(res) {
      var self = this;
      //agregamos la pregunta actual al arreglo
      self.preguntas.push(self.question['id']);
      self.respuestas.push(res['id']);
      //actualizamos la suma total
      console.log(res);
      if (res['amount'] >= 0) {
        self.monto_cotizacion = self.monto_cotizacion + parseFloat(res['amount']);
        console.log(self.monto_cotizacion);
      }
      //asignamos nueva pregunta
      self.indice = self.indice + 1;
      if (self.indice < self.questions.length) {
        self.question = self.questions[self.indice];
      }
      else {
        self.culminado = true;
      }
      //cargamos las respuestas de la nueva pregunta
      axios.get('/api/cotizacion/questions/answer/'+self.question['id']+'/')
        .then(function (response) {
          self.answers = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    enviar_solicitud: function() {
      var self = this;
      var json = {
        'email':self.email,
        'phone':self.phone,
        'message':self.message,
        'amount':self.monto_cotizacion,
        'answer':self.respuestas,
        'question':self.preguntas,
      };
      console.log(json);
      axios.post('/api/cotizacion/solicitud/save/', json)
        .then(function (response) {
          window.location.href = '/solicitud-confirmada/'
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  },
  data: {
    questions:null,
    question:null,
    answers:null,
    indice:0,
    culminado:false,
    monto_cotizacion:0,
    preguntas:[],
    respuestas:[],
    email:'',
    phone:'',
    message:'',
  },
})
