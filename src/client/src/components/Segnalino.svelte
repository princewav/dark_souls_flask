<script>
  export let id;
  export let margin = 'auto';
  export let flipped;

  const toggleFlip = () => {
    flipped = !flipped;
    window.localStorage.setItem('segnalino-' + id, flipped);
  };
</script>

<div class="container {id}">
  <div class="segnalino front" class:flipped on:click={toggleFlip} style="margin-top: {margin}">
    <img src="images/{id}.png" alt={id} />
  </div>
  <div class="segnalino back dark" class:flipped on:click={toggleFlip} style="margin-top: {margin}">
    <img src="images/{id}.png" alt={id} />
  </div>
</div>

<style>
  .container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .segnalino {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background-color: rgb(39, 37, 37);
    box-shadow: inset 0 0 14px 7px black;
    border: 3px solid #4a2910;
    backface-visibility: hidden;
    transition: transform 0.5s linear 0s;
    margin: 0;
    position: absolute;
  }
  .segnalino:hover {
    background-color: rgb(24, 12, 6);
    box-shadow: #ffbc0344 0 0 20px 10px;
    border: 3px solid #7b2c2c;
  }

  .front {
    transform: perspective(600px) rotateY(0deg);
  }
  .back {
    transform: perspective(600px) rotateY(180deg);
  }
  .front.flipped {
    transform: perspective(600px) rotateY(-180deg);
  }
  .back.flipped {
    transform: perspective(600px) rotateY(0deg);
  }

  img {
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -webkit-user-drag: none;
  }

  .dark {
    filter: brightness(40%) saturate(30%);
  }
</style>
