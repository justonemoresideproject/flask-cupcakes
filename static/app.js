const BASE_URL = "http://localhost:5000/api";

function makeCupcakes(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete-button">Delete</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
  }

  async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
  
    for (let cupcake of response.data.cupcakes) {
      let newCupcake = $(makeCupcakes(cupcake));
      $("#cupcakes-list").append(newCupcake);
    }
  }

  $("#cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#form-flavor").val();
    let size = $("#form-size").val();
    let rating = $("#form-rating").val();
    let image = $("#form-image").val();
  
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(makeCupcakes(newCupcakeResponse.data.cupcake));
    $("#cupcakelist").append(newCupcake);
    $("#cupcake-from").trigger("reset");
  });

  $("#cupcakelist").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  });
  
  
  $(showInitialCupcakes);