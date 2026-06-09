# Manual Canary Deployment Strategy

## Objective

Release a new version to a subset of users before full rollout.

---

## Architecture

Stable Deployment

Version 34

*

Canary Deployment

Version 35

---

## Components

### Stable

farm-inventory

### Canary

farm-inventory-canary

---

## Traffic Distribution

Service selects:

app=farm-inventory

Both deployments receive traffic.

---

## Validation

Endpoint:

/version

Returns:

{
"version":"34",
"track":"stable"
}

or

{
"version":"35",
"track":"canary"
}

---

## Testing

for i in {1..100}
do
curl http://service/version
done

Verified traffic reaching both versions.

---

## Lessons Learned

* Separate labels required
* Separate HPAs required
* Selector conflicts must be avoided
* Stable and Canary should scale independently
