<script>
  import Carta from './components/Carta.svelte';
  import Segnalino from './components/Segnalino.svelte';
  import Potenziamento from './components/Potenziamento.svelte';
  import Livelli from './components/Livelli.svelte';
  import Salute from './components/Salute.svelte';
  import Dadi from './components/Dadi.svelte';
  import Contatore from './components/Contatore.svelte';
  import ModalCarta from './components/ModalCarta.svelte';
  import ModalPotenziamento from './components/ModalPotenziamento.svelte';
  import Salvataggio from './components/Salvataggio.svelte';
  let showAddCardModal = false;
  let showEditCardModal = false;
  let showAddPowerupModal = false;
  let showEditPowerupModal = false;
  // let templateCard = {
  //   portata: 0,
  //   impugnatura: 2,
  //   nome: 'Ascia Grande',
  //   immagine: 'greataxe',
  //   forza: 23,
  //   destrezza: 22,
  //   intelligenza: 0,
  //   fede: 0,
  //   attacchi: [
  //     { costo: 0, icone: [{ immagine: 'dado blu', valore: 2 }] },
  //     { costo: 3, icone: [{ immagine: 'dado arancio', valore: 2 }] },
  //     {
  //       costo: 3,
  //       icone: [
  //         { immagine: 'dado blu', valore: 2 },
  //         { immagine: 'portata0', valore: 0 },
  //         { immagine: 'magico', valore: 0 },
  //       ],
  //     },
  //   ],
  //   scudo: { valore: 1, colore: 'blu' },
  //   contrasto: { valore: 0, colore: '' },
  //   schivata: 0,
  //   potenziamenti: 2,
  // };
  let stats = [
    {
      name: 'forza',
      levels: [
        [16, 1],
        [23, 0],
        [32, 0],
        [40, 0],
      ],
    },
    {
      name: 'destrezza',
      levels: [
        [9, 1],
        [16, 0],
        [25, 0],
        [35, 0],
      ],
    },
    {
      name: 'intelligenza',
      levels: [
        [8, 1],
        [15, 0],
        [23, 0],
        [30, 0],
      ],
    },
    {
      name: 'fede',
      levels: [
        [9, 1],
        [16, 0],
        [25, 0],
        [35, 0],
      ],
    },
  ];
  let templatePowerup = {
    immagine: 'heavy_gem',
    descrizione: 'Aggiungi un dado nero ad ogni attacco',
    icona: { tipo: 'dado nero', valore: 1 },
  };

  let info = {
    'arma-dx': {},
    'pot-dx1': {},
    'pot-dx2': {},
    'arma-sx': {},
    'pot-sx1': {},
    'pot-sx2': {},
    'arma-riserva': {},
    'pot-riserva1': {},
    'pot-riserva2': {},
    armatura: {},
    'pot-armatura1': {},
    'pot-armatura2': {},
  };
  let segnalinoBrace = false;
  let segnalinoEstus = false;
  let segnalinoMoneta = false;
  let segnalinoPendente = false;
  let anime = 0
  let falo = 0

  let cardData = null;
  let powerupData = null;

  const addCard = (e) => {
    showAddCardModal = true;
    cardData = JSON.stringify(e.detail);
  };
  const editCard = (e) => {
    showEditCardModal = true;
    cardData = JSON.stringify(e.detail);
  };
  const addPowerup = (e) => {
    showAddPowerupModal = true;
    powerupData = JSON.stringify(e.detail);
  };
  const editPowerup = (e) => {
    showEditPowerupModal = true;
    powerupData = JSON.stringify(e.detail);
  };

  const closeCardModal = () => {
    showAddCardModal = false;
    showEditCardModal = false;
  };
  const closePowerupModal = () => {
    showAddPowerupModal = false;
    showEditPowerupModal = false;
  };
  const saveInfoLocally = () => {
    window.localStorage.setItem('info', JSON.stringify(info));
  };

  const save = (e) => {
    const { id, ...cardData } = JSON.parse(e.detail);
    info[id] = cardData;
    closeCardModal();
    closePowerupModal();
    saveInfoLocally();
  };

  function loadGame(e) {
    let matchData = e.detail.matchData;
    info = matchData.info;
    segnalinoMoneta = JSON.parse(matchData['segnalino-moneta']);
    segnalinoPendente = JSON.parse(matchData['segnalino-pendente']);
    segnalinoBrace = JSON.parse(matchData['segnalino-brace']);
    segnalinoEstus = JSON.parse(matchData['segnalino-estus']);
    anime = parseInt(matchData.anime | '0') ;
    falo = parseInt(matchData.falo| '0');
    stats = JSON.parse(matchData.stats);
  }
</script>

{#if showAddCardModal}
  <ModalCarta {cardData} on:closecardmodal={closeCardModal} on:save={save} />
{:else if showEditCardModal}
  <ModalCarta {cardData} on:closecardmodal={closeCardModal} on:save={save} />
{/if}

{#if showAddPowerupModal}
  <ModalPotenziamento {powerupData} on:closepowerupmodal={closePowerupModal} on:save={save} />
{:else if showEditPowerupModal}
  <ModalPotenziamento {powerupData} on:closepowerupmodal={closePowerupModal} on:save={save} />
{/if}

<main>
  <section class="card-grid">
    <div class="blocco descrizione">
      <h3>CARICA BERSERK</h3>
      <p>
        Durante la sua attivazione, si potrà avanzare di un nodo in più senza spendere stamina. Il
        prossimo attaco da costo [0] avrà
        <img src="images/nodo.png" alt="nodo" height="25" width="25" />
      </p>
    </div>
    <Segnalino id={'pendente'} flipped={segnalinoPendente} />
    <Segnalino id={'estus'} flipped={segnalinoEstus} />
    <Segnalino id={'brace'} flipped={segnalinoBrace} />
    <Carta
      id="arma-riserva"
      type="arma"
      card={info['arma-riserva']}
      on:add={addCard}
      on:edit={editCard}
    />
    <Potenziamento
      id={'pot-riserva1'}
      type={'arma'}
      powerup={info['pot-riserva1']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Potenziamento
      id={'pot-riserva2'}
      type={'arma'}
      powerup={info['pot-riserva2']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Carta id="arma-dx" type="arma" card={info['arma-dx']} on:add={addCard} on:edit={editCard} />
    <Potenziamento
      id={'pot-dx1'}
      type={'arma'}
      powerup={info['pot-dx1']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Potenziamento
      id={'pot-dx2'}
      type={'arma'}
      powerup={info['pot-dx2']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Carta id="arma-sx" type="arma" card={info['arma-sx']} on:add={addCard} on:edit={editCard} />
    <Potenziamento
      id={'pot-sx1'}
      type={'arma'}
      powerup={info['pot-sx1']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Potenziamento
      id={'pot-sx2'}
      type={'arma'}
      powerup={info['pot-sx2']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Carta
      id="armatura"
      type="armatura"
      card={info['armatura']}
      on:add={addCard}
      on:edit={editCard}
    />
    <Potenziamento
      id={'pot-armatura1'}
      type={'armatura'}
      powerup={info['pot-armatura1']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
    <Potenziamento
      id={'pot-armatura2'}
      type={'armatura'}
      powerup={info['pot-armatura2']}
      on:add={addPowerup}
      on:edit={editPowerup}
    />
  </section>

  <section>
    <div class="header flex">
      <h1>GUERRIERO</h1>
      <Segnalino id={'moneta'} margin={'-50px'} flipped={segnalinoMoneta} />
    </div>
    <Livelli {stats} />
    <Salute />
  </section>

  <section>
    <div>
      <Dadi />
    </div>
    <div class="save">
      <Salvataggio on:saveas={(e) => null} on:loadedGame={loadGame} />
      on:closepowerupmodal={closePowerupModal}
    </div>
    <div class="flex">
      <Contatore id={'anime'} total={anime} />
      <Contatore id={'falo'} total={falo}/>
    </div>
  </section>
</main>

<style>
  main {
    display: grid;
    grid-template-columns: 740px 670px 2fr;
    grid-auto-rows: 100vh;
  }
  section {
    padding: 20px;
    height: 100vh;
  }
  section:nth-child(2) {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }
  section:nth-child(3) {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .flex {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  .header {
    position: relative;
    bottom: -15px;
  }
  h1 {
    font-size: 60px;
    color: white;
  }

  .descrizione img {
    position: relative;
    top: 9px;
    width: 25px;
    margin-top: -10px;
  }

  @media only screen and (max-width: 1730px) {
    main {
      grid-template-columns: 740px 670px;
    }
  }
  @media only screen and (max-width: 1400px) {
    main {
      grid-template-columns: 740px;
    }
  }
</style>
