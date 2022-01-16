<script>
  export let id;
  let total = 0;
</script>

<div class="flex">
  <span class="sign" on:click={() => (total > 0 ? (total -= 1) : 0)}>−</span>
  <div class="container">
    <img src="images/{id}.png" alt={id} />
    <span class="total">{total}</span>
  </div>
  <span class="sign" on:click={() => (total += 1)}>+</span>
</div>

<style>
  .sign {
    user-select: none;
    cursor: pointer;
    display: inline-block;
    width: 25px;
    height: 25px;
    background: #ffffff;
    color: #404040;
    border-radius: 50%;
    text-align: center;
    font-weight: bold;
    line-height: 26px;
    font-size: 26px;
  }

  .sign:hover {
    background: #cecac8;
  }
  .sign:active {
    background: #a1a1a1;
  }

  img {
    width: 100px;
    position: relative;
    top: -10px;
  }

  .flex {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .container {
    position: relative;
  }

  .total {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 30px;
    font-weight: bold;
    text-shadow: #ffffffe6 2px 1px 4px;
  }
</style>
