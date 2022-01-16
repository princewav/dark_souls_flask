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
  let templateCard = {
    portata: 0,
    impugnatura: 2,
    nome: 'Ascia Grande',
    immagine: 'greataxe',
    forza: 23,
    destrezza: 22,
    intelligenza: 0,
    fede: 0,
    attacchi: [
      { costo: 0, icone: [{ immagine: 'dado blu', valore: 2 }] },
      { costo: 3, icone: [{ immagine: 'dado arancio', valore: 2 }] },
      {
        costo: 3,
        icone: [
          { immagine: 'dado blu', valore: 2 },
          { immagine: 'portata0', valore: 0 },
          { immagine: 'magico', valore: 0 }
        ]
      }
    ],
    scudo: { valore: 1, colore: 'blu' },
    contrasto: { valore: 0, colore: '' },
    schivata: 0,
    potenziamenti: 2
  };

  let templatePowerup = {
    immagine: 'heavy_gem',
    descrizione: 'Aggiungi un dado nero ad ogni attacco',
    icona: { tipo: 'dado nero', valore: 1 }
  };

  let cardData = null;
  let powerupData = null;

  const addCard = e => {
    showAddCardModal = true;
    cardData = JSON.stringify(e.detail);
  };
  const editCard = e => {
    showEditCardModal = true;
    cardData = JSON.stringify(e.detail);
  };
  const addPowerup = e => {
    showAddPowerupModal = true;
    powerupData = JSON.stringify(e.detail);
  };
  const editPowerup = e => {
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

  const saveCard = e => {
    const { id, ...cardData } = JSON.parse(e.detail);
    templateCard = cardData;
    closeCardModal();
  };
  const savePowerup = e => {
    const { id, ...powerupData } = JSON.parse(e.detail);
    templatePowerup = powerupData;
    closePowerupModal();
  };
</script>

{#if showAddCardModal}
  <ModalCarta {cardData} on:closecardmodal={closeCardModal} on:save={saveCard} />
{:else if showEditCardModal}
  <ModalCarta {cardData} on:closecardmodal={closeCardModal} on:save={saveCard} />
{/if}

{#if showAddPowerupModal}
  <ModalPotenziamento
    {powerupData}
    on:closepowerupmodal={closePowerupModal}
    on:save={savePowerup} />
{:else if showEditPowerupModal}
  <ModalPotenziamento
    {powerupData}
    on:closepowerupmodal={closePowerupModal}
    on:save={savePowerup} />
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
    <Segnalino id={'pendente'} />
    <Segnalino id={'estus'} />
    <Segnalino id={'brace'} />
    <Carta id="arma-riserva" type="arma" on:add={addCard} on:edit={editCard} />
    <Potenziamento id={'pot-riserva1'} type={'arma'} on:add={addPowerup} on:edit={editPowerup} />
    <Potenziamento id={'pot-riserva2'} type={'arma'} on:add={addPowerup} on:edit={editPowerup} />
    <Carta id="arma-dx" type="arma" card={templateCard} on:add={addCard} on:edit={editCard} />
    <Potenziamento
      id={'pot-dx1'}
      type={'arma'}
      powerup={templatePowerup}
      on:add={addPowerup}
      on:edit={editPowerup} />
    <Potenziamento id={'pot-dx2'} type={'arma'} on:add={addPowerup} on:edit={editPowerup} />
    <Carta id="arma-sx" type="arma" on:add={addCard} on:edit={editCard} />
    <Potenziamento id={'pot-sx1'} type={'arma'} on:add={addPowerup} on:edit={editPowerup} />
    <Potenziamento id={'pot-sx2'} type={'arma'} on:add={addPowerup} on:edit={editPowerup} />
    <Carta id="armatura" type="armatura" on:add={addCard} on:edit={editCard} />
    <Potenziamento
      id={'pot-armatura1'}
      type={'armatura'}
      on:add={addPowerup}
      on:edit={editPowerup} />
    <Potenziamento
      id={'pot-armatura2'}
      type={'armatura'}
      on:add={addPowerup}
      on:edit={editPowerup} />
  </section>

  <section>
    <div class="header flex">
      <h1>GUERRIERO</h1>
      <Segnalino id={'moneta'} margin={'-30px'} />
    </div>
    <Livelli />
    <Salute />
  </section>

  <section>
    <div>
      <Dadi />
    </div>
    <div class="save">
      <Salvataggio on:saveas={e => console.log(e.detail.saveAsName)} />
    </div>
    <div class="flex">
      <Contatore id={'anime'} />
      <Contatore id={'falo'} />
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
