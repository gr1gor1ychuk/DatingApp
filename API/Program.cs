using API.Extensions;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddApplicationServices(builder.Configuration);
builder.Services.AddIdentityServices(builder.Configuration);
builder.Services.AddCors(options => 
{
    options.AddPolicy("client", policyBuilder => 
    {
        policyBuilder.AllowAnyHeader();
        policyBuilder.AllowAnyMethod();
        policyBuilder.WithOrigins("https://localhost:4200");
        policyBuilder.AllowCredentials();        
    });
});


var app = builder.Build();

// Configure the HTTP request pipeline.
// app.UseCors(x => x.AllowAnyHeader().AllowAnyMethod()
//     .WithOrigins("http://localhost:4200","https://localhost:4200)"));

app.UseCors("client");

app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();

app.Run();
